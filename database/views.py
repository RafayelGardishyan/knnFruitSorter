from operator import itemgetter
from collections import defaultdict
from django.shortcuts import render, redirect
from .models import Fruit
from .forms import FruitForm
import math


def get_most_common_item(array):
    count_dict = defaultdict(int)
    for key in array:
        count_dict[key] += 1
    key, count = max(count_dict.items(), key=itemgetter(1))
    return key


def euclidean_dist(A, B):
    return math.sqrt(sum([(A[i] - B[i]) ** 2 for i, _ in enumerate(A)]))


# Create your views here.
def get_knn(dataset_x, dataset_y, item_x, k):
    distances = [euclidean_dist(item_x, ds) for ds in dataset_x]
    sorted_distances = sort(distances)
    closest_knn = [distances.index(sorted_distances[i]) for i in range(0, k)] if k > 1 else [
        distances.index(min(distances))]
    closest_labels_knn = [dataset_y[x] for x in closest_knn]
    item = get_most_common_item(closest_labels_knn)
    return item


def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less) + equal + sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


def index(request):
    count = Fruit.objects.count()
    return render(request, 'index.html', {'count': count})


def enter(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FruitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # f = Fruit()
            x = []
            y = []
            fruits = Fruit.objects.all()
            for item in fruits:
                x.append([item.color, item.size, item.texture, item.shape])
                y.append(item.name)

            ftype = get_knn(x, y, [int(form.cleaned_data['color']),
                                   int(form.cleaned_data['size']),
                                   int(form.cleaned_data['texture']),
                                   int(form.cleaned_data['shape'])], k=3)

            f = Fruit()
            f.name = ftype
            f.size = int(form.cleaned_data['size'])
            f.color = int(form.cleaned_data['color'])
            f.shape = int(form.cleaned_data['shape'])
            f.texture = int(form.cleaned_data['texture'])
            f.save()
            return render(request, 'sorted.html', {"type": ftype, "id": f.id})

            # if a GET (or any other method) we'll create a blank form
    else:
        form = FruitForm()

    return render(request, 'input.html', {'form': form})

def edit(request, id):
    if request.method == "POST":
        f = Fruit.objects.get(id=id)
        f.name = request.POST['name'].lower().capitalize()
        f.save()
        return redirect('/view/' + str(id))
    else:
        return render(request, "edit.html", {})

def view(request, id):
    ftype = Fruit.objects.get(id=id).name
    return render(request, 'sorted.html', {"type": ftype, "id": id})
