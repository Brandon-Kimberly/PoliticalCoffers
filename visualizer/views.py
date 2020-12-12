from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404, JsonResponse
from django.db.models import Sum
from .models import Candidate, Donation
from django.views.generic import TemplateView
import os
import sys

def home(request):
    return render(request, 'visualizer/home.html')

def top_spenders_chart(request):
    labels = []
    data = []
    try:
        yearp = str(request.session['yeare'])
    except:
        yearp = "0000"

    if (yearp == "0000"):
        queryset = Candidate.objects.values('name').annotate(total_earned=Sum('total_spent_amount')).order_by('-total_spent_amount')[:10]
    else:
        queryset = Candidate.objects.filter(year=yearp).values('name').annotate(total_earned=Sum('total_donation_amount')).order_by('-total_donation_amount')[:10]

    for entry in queryset:
        labels.append(entry['name'])
        data.append(entry['total_earned'])

    return JsonResponse(data = {
        'labels' : labels,
        'data' : data,
        })

def render_top_spenders_chart(request):
    if (request.method == 'POST'):
        request.session['yeare'] = request.POST['year']
    return render(request, 'visualizer/spending-chart.html')

def spending_pie(request):
    labels = []
    data = []
    total_d = 0
    total_r = 0

    try:
        yearp = str(request.session['years'])
    except:
        yearp = "0000"

    if yearp == "0000":
        queryset = Candidate.objects.values('name', 'party').annotate(total_spent=Sum('total_spent_amount')).order_by('-total_spent_amount')
    else:
        queryset = Candidate.objects.filter(year=yearp).values('name', 'party').annotate(total_spent=Sum('total_spent_amount')).order_by('-total_spent_amount')

    for candidate in queryset:
        if (candidate['party'] == 'DEM'):
            total_d += candidate['total_spent']
        elif (candidate['party'] == 'REP'):
            total_r += candidate['total_spent']

    labels.append("Democrat")
    data.append(total_d)
    labels.append("Republican")
    data.append(total_r)

    return JsonResponse(data = {
        'labels' : labels,
        'data' : data,
        })

def render_spending_pie(request):
    if (request.method == 'POST'):
        request.session['years'] = request.POST['year']
    return render(request, 'visualizer/spending-pie.html')

def donors_pie(request):
    labels = []
    data = []
    over = 0
    under = 0

    try:
        target = float(request.session['target'])
    except:
        target = 100

    print(str(target), file=sys.stderr)

    queryset = Donation.objects.values('amount')[:1000000];

    for donation in queryset:
        if (donation['amount'] >= target):
            over += 1
        else:
            under += 1

    labels.append("Over target amount")
    data.append(over)
    labels.append("Under target amount")
    data.append(under)

    return JsonResponse(data = {
        'labels' : labels,
        'data' : data,
        })

def render_donors_pie(request):
    if (request.method == 'POST'):
        request.session['target'] = request.POST['target']
    return render(request, 'visualizer/donors-pie.html')

def render_donors_pie_base(request):
    return render(request, 'visualizer/donors-pie-base.html')

def load_data(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    year = 1980
    while year <= 2020:
        print(str(year), file=sys.stderr)
        path_str = 'candidates' + str(year) + '.txt'
        file_path = os.path.join(module_dir, path_str)

        file = open(file_path, 'r')
        lines = [line.strip() for line in file]

        for line in lines:
            try:
                info = line.split('|')
                namep = info[1] + ' ' + str(year)
                partyp = info[4]
                total_donation_amountp = info[5]
                total_spent_amountp = info[7]
                beginning_cashp = info[9]
                ending_cashp = info[10]
                total_ind_contribp = info[17]
                yearp = str(year)
                Candidate.objects.create(name=namep, party=partyp, total_donation_amount=total_donation_amountp,
                                         total_spent_amount=total_spent_amountp, beginning_cash=beginning_cashp,
                                         ending_cash = ending_cashp, total_ind_contrib=total_ind_contribp,
                                         year = yearp)
            except Exception as e:
                print("it failed" + ": " + str(e), file=sys.stderr)
                print(line)

        year += 2
        file.close()

    return render(request, 'visualizer/base.html')