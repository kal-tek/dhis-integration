from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from unicodedata import name
import mysql.connector
from mysql.connector import errorcode



def table_view(request):
    """
    View for the table page.
    """
    # Connect to MySQL database

    try:
        cnx = mysql.connector.connect(
            user="",
            password="",
            host="",  # use the name of the MySQL container in Docker network
            database="",
            port=3307,
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise Exception("Failed to connect to MySQL")

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM person")
    result = cursor.fetchall()



    # Create your views here.
    return render(request, "table.html", {})


@csrf_exempt
def send_to_dhis(request):
    """
    View for the table page.
    """
    if request.method == "POST":
        data = request.POST.get("data")
        data["month"] = data["month"].replace("-", "")

    return JsonResponse({"status": "ok"})
