import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backend_bases import key_press_handler
from IPython.display import display, clear_output
import ipywidgets as widgets
from IPython.display import display


################################################################
################################################################
def insertion_sort(tablica, left=0, right=None):
    if right is None:
        right = len(tablica) - 1

    for i in range(left + 1, right + 1):
        j = i
        while j > left and tablica[j] < tablica[j - 1]:
            tablica[j], tablica[j - 1] = tablica[j - 1], tablica[j]
            j -= 1


def merge(tablica, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid

    left_half = tablica[left : mid + 1].copy()
    right_half = tablica[mid + 1 : right + 1].copy()

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_half[i] <= right_half[j]:
            tablica[k] = left_half[i]
            i += 1
        else:
            tablica[k] = right_half[j]
            j += 1
        k += 1

    while i < len_left:
        tablica[k] = left_half[i]
        i += 1
        k += 1

    while j < len_right:
        tablica[k] = right_half[j]
        j += 1
        k += 1


def tim_sort(tablica: MonitorowanaTablica):
    min_run = 32
    n = len(tablica)

    for i in range(0, n, min_run):
        insertion_sort(tablica, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(tablica, left, mid, right)

        size = 2 * size


################################################################


################################################################
def plot_sorting_animation(tablica: MonitorowanaTablica, algorithm_name: str, fps=60):
    """Plots the sorting animation for the given data.

    Args:
    tablica (MonitorowanaTablica): The array being sorted.
    algorithm_name (str): Name of the sorting algorithm.
    fps (int): Frames per second for the animation.
    """
    plt.rcParams["font.size"] = 16
    fig, ax = plt.subplots(figsize=(16, 8))
    container = ax.bar(
        range(len(tablica)), tablica.pelne_kopie[0], align="edge", width=0.8
    )
    fig.suptitle(f"Sorting: {algorithm_name}")
    ax.set(xlabel="Index", ylabel="Value")
    ax.set_xlim([0, len(tablica)])
    txt = ax.text(0.01, 0.99, "", ha="left", va="top", transform=ax.transAxes)

    def update(frame: int):
        """Updates the histogram for each frame of the animation.

        Args:
        frame (int): The current frame number.
        """
        txt.set_text(f"Operations = {frame}")
        for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
            rectangle.set_height(height)
            rectangle.set_color("darkblue")

        idx, op = tablica.aktywnosc(frame)
        if op == "get":
            container.patches[idx].set_color("green")
        elif op == "set":
            container.patches[idx].set_color("red")

        return (txt, *container)

    ani = FuncAnimation(
        fig,
        update,
        frames=range(len(tablica.pelne_kopie)),
        blit=True,
        interval=1000.0 / fps,
        repeat=False,
    )

    print("INFO: Animation pending... Press SPACE to skip")

    # Add space key event listener
    def on_space(event):
        try:
            if event.key == " ":
                ani.event_source.stop()
                clear_output(wait=True)
                plt.close(fig)
                # Display the final state of the array
                plt.bar(
                    range(len(tablica)),
                    tablica.pelne_kopie[-1],
                    align="edge",
                    width=0.8,
                    color="darkblue",
                )
                plt.title(f"Final State: {algorithm_name}")
                plt.xlabel("Index")
                plt.ylabel("Value")
                plt.show()
                print("INFO: Animation skipped!")
        except AttributeError:
            print("ERROR: Cannot skip finished animation!")

    fig.canvas.mpl_connect("key_press_event", on_space)
    print("INFO: Animation Finished! Close plot window to continue...")
    plt.show()


################################################################


################################################################
def main():
    N = 50  # Number of elements, can be changed
    FPS = 480000  # Frames per second for the animation
    results = open("results.txt", "a")  # File that stores the time results
    
    # Initialize the array
    tablicaR = MonitorowanaTablica(0, 1000, N, "R")
    tablicaS = MonitorowanaTablica(0, 1000, N, "S")
    tablicaA = MonitorowanaTablica(0, 1000, N, "A")
    tablicaT = MonitorowanaTablica(0, 1000, N, "T")

    # Perform the sorting
    #####TIM##########
    results.write(f"Sorting: Tim\n")

    t0 = time.perf_counter()
    tim_sort(tablicaR)
    delta_t = time.perf_counter() - t0

    results.write(
        f"R: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaR.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    tim_sort(tablicaS)
    delta_t = time.perf_counter() - t0

    results.write(
        f"S: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaS.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    tim_sort(tablicaA)
    delta_t = time.perf_counter() - t0

    results.write(
        f"A: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaA.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    tim_sort(tablicaT)
    delta_t = time.perf_counter() - t0

    results.write(
        f"T: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaT.pelne_kopie):.0f}.\n"
    )

    # Plot the sorting animation
    plot_sorting_animation(tablicaR, "R: Tim", FPS)
    plot_sorting_animation(tablicaS, "S: Tim", FPS)
    plot_sorting_animation(tablicaA, "A: Tim", FPS)
    plot_sorting_animation(tablicaT, "T: Tim", FPS)

    results.write("\n\n")

    results.close()


################################################################

################################################################
# Call the main function
if __name__ == "__main__":
    main()
