from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Item, ItemInfo
from .forms import ItemModelForm


@login_required
def getItems(request):
  items = Item.objects.filter(created_by=request.user)
  print(items)

  context = {
      'items': items
  }
  return render(request, 'inventory/items.html', context)


@login_required
def getItem(request, pk):
  item = Item.objects.get(pk=pk, created_by=request.user)
  item_info = ItemInfo.objects.filter(item=item).first()

  context = {
      'item': item,
      'info': item_info
  }
  return render(request, 'inventory/item.html', context)


@login_required
def addItem(request):
  form = ItemModelForm
  if request.method == 'POST':
    form = ItemModelForm(request.POST)
    if form.is_valid():
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()
      return redirect('items')
  context = {
      'form': form
  }
  return render(request, 'inventory/addItem.html', context)


@login_required
def deleteItem(request, pk):
  Item.objects.filter(pk=pk, created_by=request.user).delete()
  return redirect('items')
