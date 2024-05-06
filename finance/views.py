import csv
import io

from typing import Any
from django.db.models import F
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import date
from decimal import *
from rest_framework import viewsets

from .models import Transaction, Category
from .forms import UploadTransactionForm
from .serializers import TransactionSerializer, CategorySerializer


@login_required
def index(request):
    if request.method == "POST":
        form = UploadTransactionForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
        else:
            form = UploadTransactionForm()

    context = {
            "form": UploadTransactionForm()
        }
    return render(request, "finance/index.html", context)

def logout_view(request):
    logout(request)
    return redirect("finance:index")

def upload_transactions(request):
    if request.method == "POST":
        form = UploadTransactionForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
        else:
            form = UploadTransactionForm()

    context = {
            "form": UploadTransactionForm()
        }
    return render(request, "finance/upload_transactions.html", context)


def handle_uploaded_file(file):
    getcontext().prec = 2
    print("Processing csv...")
    data = file.read().decode("ascii").splitlines()
    reader = csv.DictReader(data, delimiter=";")
    for row in reader:
        split_date = row["Date"].split("/")
        transaction = Transaction.objects.create(
            account = row["Account number"],
            currency = row["Currency"],
            amount = Decimal(float(row["Amount"].replace(',', '.'))),
            date = date(int(split_date[2]), int(split_date[1]), int(split_date[0])),
            balance = Decimal(row["Balance"].replace(',', '.')),
            counterparty_name = row["Counterparty name"],
            counterparty_account = row["counterparty's account number"],
            description = row["Description"],
            category = Category.objects.filter(name="Other")[0],
        )
        transaction.save()

class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("-id")
    serializer_class = TransactionSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer