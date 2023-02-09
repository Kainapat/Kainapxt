#heap sort
# พรธวัล คุ้มภัย INE 6506022610031
# กายณภัทร สุวรรณโชติ INE 6506022620052
# เอกตะวัน พุทธมงคล INE 6506022620133
# ศุกลวัฒน์ ชูเลิศ INE 6506022620125 

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def collect_scores():
    num_students = int(input("Enter number of students: "))
    scores = []
    for i in range(num_students):
        score = int(input("Enter score for student {}: ".format(i+1)))
        scores.append(score)
    heap_sort(scores)
    print("Sorted scores in descending order:", scores[::-1])
    print("Top 3 highest scores:", scores[-1:-4:-1])
    print("Top 3 lowest scores:", scores[:3])
    target_score = int(input("Enter target score to search: "))
    if scores.count(target_score) > 0:
        print("Score found,:", scores.count(target_score),'Students')
    else:
        print("Score not found")

if __name__ == "__main__":
    collect_scores()