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
def quick_sort(tablica: MonitorowanaTablica):
    stack = [(0, len(tablica) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(tablica, low, high)

            # Push the subarrays onto the stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))


def partition(tablica, low, high):
    pivot = tablica[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and tablica[left] <= pivot:
            left = left + 1

        while tablica[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            # Swap elements at left and right indices
            tablica[left], tablica[right] = tablica[right], tablica[left]

    # Swap pivot with the right element
    tablica[low], tablica[right] = tablica[right], tablica[low]

    return right


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
    #####QUICK##########
    results.write(f"Sorting: Quick\n")

    t0 = time.perf_counter()
    quick_sort(tablicaR)
    delta_t = time.perf_counter() - t0

    results.write(
        f"R: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaR.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    quick_sort(tablicaS)
    delta_t = time.perf_counter() - t0

    results.write(
        f"S: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaS.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    quick_sort(tablicaA)
    delta_t = time.perf_counter() - t0

    results.write(
        f"A: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaA.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    quick_sort(tablicaT)
    delta_t = time.perf_counter() - t0

    results.write(
        f"T: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaT.pelne_kopie):.0f}.\n"
    )

    # Plot the sorting animation
    plot_sorting_animation(tablicaR, "R: Quick", FPS)
    plot_sorting_animation(tablicaS, "S: Quick", FPS)
    plot_sorting_animation(tablicaA, "A: Quick", FPS)
    plot_sorting_animation(tablicaT, "T: Quick", FPS)

    results.write("\n\n")

    results.close()


################################################################

################################################################
# Call the main function
if __name__ == "__main__":
    main()
