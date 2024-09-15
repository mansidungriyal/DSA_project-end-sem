import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr  # Yield after each comparison to visualize step by step


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr  # Yield after each shift for visualization
        arr[j + 1] = key
        yield arr  # Yield after each insertion


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr  # Yield after each selection and swap


# Main visualization function

def visualize_sorting(arr, algorithm_generator):
    fig, ax = plt.subplots()
    ax.set_title("Sorting Algorithm Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(new_arr, rects, iteration):
        for rect, val in zip(rects, new_arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Number of operations: {iteration[0]}")

    anim = animation.FuncAnimation(fig, update_fig, fargs=(bar_rects, iteration),
                                   frames=algorithm_generator, interval=50,
                                   repeat=False)
    plt.show()


# Main function

if __name__ == "__main__":

    N = 20  # Adjust N for a larger array
    arr = [random.randint(1, 20) for _ in range(N)]  # Larger random numbers

    # Instructions for user input
    print("CHOOSE A SORTING ALGORITHM")
    print("1. BUBBLE SORT")
    print("2. INSERTION SORT")
    print("3. SELECTION SORT")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        algorithm_generator = bubble_sort(arr)
    elif choice == 2:
        algorithm_generator = insertion_sort(arr)
    elif choice == 3:
        algorithm_generator = selection_sort(arr)
    else:
        print("Invalid choice!")
        exit()

    # Visualize the sorting process
    visualize_sorting(arr, algorithm_generator)
#type:ignore