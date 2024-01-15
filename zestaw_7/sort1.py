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
'''
def insertion_sort(tablica: MonitorowanaTablica):
    """Performs the insertion sort on the given array.

    Args:
    tablica (MonitorowanaTablica): The array to be sorted.
    """
    i = 1
    while i < len(tablica):
        j = i
        while j > 0 and tablica[j - 1] > tablica[j]:
            tablica[j - 1], tablica[j] = tablica[j], tablica[j - 1]
            j -= 1
        i += 1'''


################################################################
################################################################
def bubble_sort(tablica: MonitorowanaTablica):
    n = len(tablica)

    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                swapped = True
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

        if not swapped:
            return


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
    results.truncate(0)

    # Initialize the array
    tablicaR = MonitorowanaTablica(0, 1000, N, "R")
    tablicaS = MonitorowanaTablica(0, 1000, N, "S")
    tablicaA = MonitorowanaTablica(0, 1000, N, "A")
    tablicaT = MonitorowanaTablica(0, 1000, N, "T")

    # Perform the sorting
    results.write(f"Sorting: Bubble\n")

    t0 = time.perf_counter()
    bubble_sort(tablicaR)
    delta_t = time.perf_counter() - t0

    results.write(
        f"R: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaR.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    bubble_sort(tablicaS)
    delta_t = time.perf_counter() - t0

    results.write(
        f"S: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaS.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    bubble_sort(tablicaA)
    delta_t = time.perf_counter() - t0

    results.write(
        f"A: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaA.pelne_kopie):.0f}.\n"
    )

    t0 = time.perf_counter()
    bubble_sort(tablicaT)
    delta_t = time.perf_counter() - t0

    results.write(
        f"T: Array sorted in {delta_t*1000:.1f} ms. Number of operations: {len(tablicaT.pelne_kopie):.0f}.\n"
    )

    # Plot the sorting animation
    plot_sorting_animation(tablicaR, "R: Bubble", FPS)
    plot_sorting_animation(tablicaS, "S: Bubble", FPS)
    plot_sorting_animation(tablicaA, "A: Bubble", FPS)
    plot_sorting_animation(tablicaT, "T: Bubble", FPS)

    results.write("\n\n")

    results.close()


################################################################


################################################################
# Call the main function
if __name__ == "__main__":
    main()