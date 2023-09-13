from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client
from .forms import AddClientForm


@login_required
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST, user=request.user)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            messages.success(request, 'Новая запись добавлена!')
            return redirect('home')
    else:
        form = AddClientForm(user=request.user)
    return render(request, 'clients/add_client.html', {'form': form})


@login_required
def view_client(request, pk):
    client = Client.objects.filter(pk=pk, user=request.user)
    return render(request, 'clients/view_client.html', {'client': client})


@login_required
def update_info(request, pk):
    client = get_object_or_404(Client, pk=pk, user=request.user)

    if request.method == 'GET':
        context = {'form': AddClientForm(instance=client, user=request.user), 'pk': pk}
        return render(request, 'clients/update_client.html', context)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client, user=request.user)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            messages.success(request, 'Запись изменена!')
            return redirect('home')
    return render(request, 'clients/update_client.html', {'form': form})


@login_required   
def del_client(request, pk):
    client = Client.objects.filter(pk=pk, user=request.user)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Запись удалена!')
        return redirect('home')


def send_message(request, id):
    client = Client.objects.get(id=id, user=request.user)
    phone_number = client.phone
    for i in ' +()-':
        if i in phone_number:
            phone_number = phone_number.replace(i, '')
    return redirect(f'https://web.whatsapp.com/send?phone={phone_number}')
