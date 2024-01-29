from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):

    # new_worker = Worker(name='Сергей', second_name='Сергеев', salary=90000)
    # # или Worker.objects.create(name='Сергей', second_name='Сергеев', salary=90000)
    # new_worker.save()

    # Worker.objects.get(id=5).delete()

    # worker_to_change = Worker.objects.get(id=5) # только для одного объекта
    # # print(worker_to_change)
    # worker_to_change.second_name = 'Черкасов'
    # worker_to_change.save()
    # # # или Worker.objects.filter(id=5).update(second_name='Черкасов') - может обновить несколько объектов

    all_workers = Worker.objects.all()

    some_dictionary = {'data': 'Куку', 'data2': 'Угу'}

    # print(all_workers)
    #
    # workers_filtered = Worker.objects.filter(salary=60000)
    # print(workers_filtered)

    # for i in all_workers:
    #     print(f'ID: {i.id}, Имя: {i.name}, Фамилия: {i.second_name}, Зарплата: {i.salary}')

    return render(request, 'index.html', context={'data': all_workers})
