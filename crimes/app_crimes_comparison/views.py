from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import matplotlib.pyplot as plt

# Zdefiniowane funkcje do przekazania do urls. każda funckaj odpowida urls
@login_required()
def dane(request):
    return render(request, "dane.html")


def login(request):
    return render(request, "login.html")


def sign_up(request):
    return render(request, "sign_up.html")


def index(request):
    return render(request, "index.html")


def my_login_view(request):
    return LoginView.as_view(template_name='login.html')(request)


csv_files = ['data/Crimes-2021.csv', 'data/Crimes-2022.csv', 'data/Crimes-2023.csv', 'data/Crimes-2024.csv']
dfs = [pd.read_csv(csv_file, delimiter=';') for csv_file in csv_files]


def dane_view(request):
    return render(request, 'dane.html')


def generate_wykres(request):
    data_lengths = [len(df) for df in dfs]
    years = ['2021', '2022', '2023', '2024']
    positions = range(len(data_lengths))

    width = 0.2
    plt.bar(positions, data_lengths, width=width, color='r')
    plt.xticks(positions, years, rotation=80)
    plt.title('Liczba przestępst w poszczególnych latach w Chicago', fontweight='bold', fontsize=15, x=0.5, y=1.1)
    plt.ylabel('Ilość przestępstw', fontweight='bold', fontsize=15, labelpad=20)

    # Zapisz wykres jako obrazek
    image_path = 'media/images/wykres.png'
    plt.savefig(image_path)
    plt.close()

    return JsonResponse({'image_url': '/' + image_path})
