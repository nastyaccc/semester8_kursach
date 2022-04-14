from datetime import datetime, timedelta
from django.shortcuts import render, redirect

from kursach.models import AircraftType, CarrierFlights, Carriers, City, ClientOrders, ClientTours, Clients, Country, EmployeeMotions, Employees, Hotel, HotelType, OrderType, Position, ReasonForTransfer, Routes
from django.views.decorators.csrf import csrf_exempt


def positions(request):
    return render(request, 'model_list.html', {'name': 'position', 'models': Position.objects.all()})


@csrf_exempt
def add_position(request):
    if request.method == 'POST':
        model = Position()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/positions/')
    else:
        return render(request, 'model_add.html', {'type': 'position'})


@csrf_exempt
def edit_position(request, id: int):
    if request.method == 'POST':
        model = Position.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/positions/')
    else:
        return render(request, 'model_edit.html', {'type': 'position', 'model': Position.objects.get(id=id)})


@csrf_exempt
def delete_position(request, id: int):
    model = Position.objects.get(id=id)
    model.delete()
    return redirect('/positions/')


def order_types(request):
    return render(request, 'model_list.html', {'name': 'order_type', 'models': OrderType.objects.all()})


@csrf_exempt
def add_order_type(request):
    if request.method == 'POST':
        model = OrderType()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/order_types/')
    else:
        return render(request, 'model_add.html', {'type': 'order_type'})


@csrf_exempt
def edit_order_type(request, id: int):
    if request.method == 'POST':
        model = OrderType.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/order_types/')
    else:
        return render(request, 'model_edit.html', {'type': 'order_type', 'model': OrderType.objects.get(id=id)})


@csrf_exempt
def delete_order_type(request, id: int):
    model = OrderType.objects.get(id=id)
    model.delete()
    return redirect('/order_types/')


def reasons_for_transfer(request):
    return render(request, 'model_list.html', {'name': 'reason_for_transfer', 'models': ReasonForTransfer.objects.all()})


@csrf_exempt
def add_reason_for_transfer(request):
    if request.method == 'POST':
        model = ReasonForTransfer()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/reasons_for_transfer/')
    else:
        return render(request, 'model_add.html', {'type': 'reason_for_transfer'})


@csrf_exempt
def edit_reason_for_transfer(request, id: int):
    if request.method == 'POST':
        model = ReasonForTransfer.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/reasons_for_transfer/')
    else:
        return render(request, 'model_edit.html', {'type': 'reason_for_transfer', 'model': ReasonForTransfer.objects.get(id=id)})


@csrf_exempt
def delete_reason_for_transfer(request, id: int):
    model = ReasonForTransfer.objects.get(id=id)
    model.delete()
    return redirect('/reasons_for_transfer/')


def countries(request):
    return render(request, 'model_list.html', {'name': 'country', 'models': Country.objects.all()})


@csrf_exempt
def add_country(request):
    if request.method == 'POST':
        model = Country()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/countries/')
    else:
        return render(request, 'model_add.html', {'type': 'country'})


@csrf_exempt
def edit_country(request, id: int):
    if request.method == 'POST':
        model = Country.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/countries/')
    else:
        return render(request, 'model_edit.html', {'type': 'country', 'model': Country.objects.get(id=id)})


@csrf_exempt
def delete_country(request, id: int):
    model = Country.objects.get(id=id)
    model.delete()
    return redirect('/countries/')


def cities(request):
    return render(request, 'model_list.html', {'name': 'city', 'models': City.objects.all()})


@csrf_exempt
def add_city(request):
    if request.method == 'POST':
        model = City()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/cities/')
    else:
        return render(request, 'model_add.html', {'type': 'city'})


@csrf_exempt
def edit_city(request, id: int):
    if request.method == 'POST':
        model = City.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/cities/')
    else:
        return render(request, 'model_edit.html', {'type': 'city', 'model': City.objects.get(id=id)})


@csrf_exempt
def delete_city(request, id: int):
    model = City.objects.get(id=id)
    model.delete()
    return redirect('/cities/')


def hotel_types(request):
    return render(request, 'model_list.html', {'name': 'hotel_type', 'models': HotelType.objects.all()})


@csrf_exempt
def add_hotel_type(request):
    if request.method == 'POST':
        model = HotelType()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/hotel_types/')
    else:
        return render(request, 'model_add.html', {'type': 'hotel_type'})


@csrf_exempt
def edit_hotel_type(request, id: int):
    if request.method == 'POST':
        model = HotelType.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/hotel_types/')
    else:
        return render(request, 'model_edit.html', {'type': 'hotel_type', 'model': HotelType.objects.get(id=id)})


@csrf_exempt
def delete_hotel_type(request, id: int):
    model = HotelType.objects.get(id=id)
    model.delete()
    return redirect('/hotel_types/')


def carriers(request):
    return render(request, 'model_list.html', {'name': 'carrier', 'models': Carriers.objects.all()})


@csrf_exempt
def add_carrier(request):
    if request.method == 'POST':
        model = Carriers()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/carriers/')
    else:
        return render(request, 'model_add.html', {'type': 'carrier'})


@csrf_exempt
def edit_carrier(request, id: int):
    if request.method == 'POST':
        model = Carriers.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/carriers/')
    else:
        return render(request, 'model_edit.html', {'type': 'carrier', 'model': Carriers.objects.get(id=id)})


@csrf_exempt
def delete_carrier(request, id: int):
    model = Carriers.objects.get(id=id)
    model.delete()
    return redirect('/carriers/')


def aircraft_types(request):
    return render(request, 'model_list.html', {'name': 'aircraft_type', 'models': AircraftType.objects.all()})


@csrf_exempt
def add_aircraft_type(request):
    if request.method == 'POST':
        model = AircraftType()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/aircraft_types/')
    else:
        return render(request, 'model_add.html', {'type': 'aircraft_type'})


@csrf_exempt
def edit_aircraft_type(request, id: int):
    if request.method == 'POST':
        model = AircraftType.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/aircraft_types/')
    else:
        return render(request, 'model_edit.html', {'type': 'aircraft_type', 'model': AircraftType.objects.get(id=id)})


@csrf_exempt
def delete_aircraft_type(request, id: int):
    model = AircraftType.objects.get(id=id)
    model.delete()
    return redirect('/aircraft_types/')


def employees(request):
    return render(request, 'employee_list.html', {'name': 'employee', 'models': Employees.objects.all()})


@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        model = Employees()
        model.s_name = request.POST.get('s_name')
        model.f_name = request.POST.get('f_name')
        model.t_name = request.POST.get('t_name')
        model.address = request.POST.get('address')
        model.phone = request.POST.get('phone')
        model.hb_day = datetime.fromisoformat(request.POST.get('hb_day')) if request.POST.get('hb_day') else datetime.fromisoformat('1970-01-01')
        model.id_position = int(request.POST.get('id_position')) or None
        model.salary = float(request.POST.get('salary'))
        model.save()
        return redirect('/employees/')
    else:
        return render(request, 'employee_add.html', {'type': 'employee', 'positions': Position.objects.all()})


@csrf_exempt
def edit_employee(request, id: int):
    if request.method == 'POST':
        model = Employees.objects.get(id=id)
        model.s_name = request.POST.get('s_name')
        model.f_name = request.POST.get('f_name')
        model.t_name = request.POST.get('t_name')
        model.address = request.POST.get('address')
        model.phone = request.POST.get('phone')
        model.hb_day = datetime.fromisoformat(request.POST.get('hb_day')) if request.POST.get('hb_day') else datetime.fromisoformat('1971-01-01')
        model.id_position = int(request.POST.get('id_position')) or None
        model.salary = float(request.POST.get('salary'))
        model.save()
        return redirect('/employees/')
    else:
        return render(request, 'employee_edit.html', {'type': 'employee', 'model': Employees.objects.get(id=id), 'positions': Position.objects.all()})


@csrf_exempt
def delete_employee(request, id: int):
    model = Employees.objects.get(id=id)
    model.delete()
    return redirect('/employees/')


def employee_motions(request):
    return render(request, 'employee_motion_list.html', {'name': 'employee_motion', 'models': EmployeeMotions.objects.all()})


@csrf_exempt
def add_employee_motion(request):
    if request.method == 'POST':
        model = EmployeeMotions()
        model.id_employee = int(request.POST.get('id_employee')) or None
        model.id_position = int(request.POST.get('id_position')) or None
        model.id_reason = int(request.POST.get('id_reason')) or None
        model.order = request.POST.get('order')
        model.date_order = datetime.fromisoformat(request.POST.get('date_order')) if request.POST.get('date_order') else datetime.fromisoformat('2022-01-01')
        model.save()
        return redirect('/employee_motions/')
    else:
        return render(request, 'employee_motion_add.html', {'type': 'employee_motion', 'positions': Position.objects.all(), 'employees': Employees.objects.all(), 'reasons': ReasonForTransfer.objects.all()})


@csrf_exempt
def edit_employee_motion(request, id: int):
    if request.method == 'POST':
        model = EmployeeMotions.objects.get(id=id)
        model.id_employee = int(request.POST.get('id_employee')) or None
        model.id_position = int(request.POST.get('id_position')) or None
        model.id_reason = int(request.POST.get('id_reason')) or None
        model.order = request.POST.get('order')
        model.date_order = datetime.fromisoformat(request.POST.get('date_order')) if request.POST.get(
            'date_order') else datetime.fromisoformat('2022-01-01')
        model.save()
        return redirect('/employee_motions/')
    else:
        return render(request, 'employee_motion_edit.html', {'type': 'employee_motion', 'model': EmployeeMotions.objects.get(id=id), 'employees': Employees.objects.all(), 'reasons': ReasonForTransfer.objects.all(), 'positions': Position.objects.all()})


@csrf_exempt
def delete_employee_motion(request, id: int):
    model = EmployeeMotions.objects.get(id=id)
    model.delete()
    return redirect('/employee_motions/')


def routes(request):
    return render(request, 'model_list.html', {'name': 'route', 'models': Routes.objects.all()})


@csrf_exempt
def add_route(request):
    if request.method == 'POST':
        model = Routes()
        model.name = request.POST.get('name')
        model.id_country = int(request.POST.get('id_country')) or None
        model.id_city = int(request.POST.get('id_city')) or None
        model.id_hotel = int(request.POST.get('id_hotel')) or None
        model.id_carrier = int(request.POST.get('id_carrier')) or None
        model.id_employee = int(request.POST.get('id_employee')) or None
        model.save()
        return redirect('/routes/')
    else:
        return render(request, 'route_add.html', {'type': 'route', 'countries': Country.objects.all(), 'cities': City.objects.all(), 'hotels': Hotel.objects.all(), 'carriers': Carriers.objects.all(), 'employees': Employees.objects.all()})


@csrf_exempt
def edit_route(request, id: int):
    if request.method == 'POST':
        model = Routes.objects.get(id=id)
        model.name = request.POST.get('name')
        model.id_country = int(request.POST.get('id_country')) or None
        model.id_city = int(request.POST.get('id_city')) or None
        model.id_hotel = int(request.POST.get('id_hotel')) or None
        model.id_carrier = int(request.POST.get('id_carrier')) or None
        model.id_employee = int(request.POST.get('id_employee')) or None
        model.save()
        return redirect('/routes/')
    else:
        return render(request, 'route_edit.html',
                      {'type': 'route', 'countries': Country.objects.all(), 'cities': City.objects.all(),
                       'hotels': Hotel.objects.all(), 'carriers': Carriers.objects.all(),
                       'employees': Employees.objects.all(), 'model': Routes.objects.get(id=id)})


@csrf_exempt
def delete_route(request, id: int):
    model = Routes.objects.get(id=id)
    model.delete()
    return redirect('/routes/')


def hotels(request):
    return render(request, 'model_list.html', {'name': 'hotel', 'models': Hotel.objects.all()})


@csrf_exempt
def add_hotel(request):
    if request.method == 'POST':
        model = Hotel()
        model.name = request.POST.get('name')
        model.id_hotel_type = int(request.POST.get('id_hotel_type')) or None
        model.save()
        return redirect('/hotels/')
    else:
        return render(request, 'hotel_add.html', {'type': 'hotel', 'hotel_types': HotelType.objects.all()})


@csrf_exempt
def edit_hotel(request, id: int):
    if request.method == 'POST':
        model = Hotel.objects.get(id=id)
        model.name = request.POST.get('name')
        model.id_hotel_type = int(request.POST.get('id_hotel_type')) or None
        model.save()
        return redirect('/hotels/')
    else:
        return render(request, 'hotel_edit.html', {'type': 'hotel', 'hotel_types': HotelType.objects.all(), 'model': Hotel.objects.get(id=id)})


@csrf_exempt
def delete_hotel(request, id: int):
    model = Hotel.objects.get(id=id)
    model.delete()
    return redirect('/hotels/')


def carrier_flights(request):
    return render(request, 'model_list.html', {'name': 'carrier_flight', 'models': CarrierFlights.objects.all()})


@csrf_exempt
def add_carrier_flight(request):
    if request.method == 'POST':
        model = CarrierFlights()
        model.id_carrier = int(request.POST.get('id_carrier')) or None
        model.numb_flight = int(request.POST.get('numb_flight'))
        model.date_f = datetime.fromisoformat(request.POST.get('date_f')) if request.POST.get('date_f') else datetime.fromisoformat('2022-01-01')
        model.id_aircraft_type = int(request.POST.get('id_aircraft_type')) or None
        model.free_seats = int(request.POST.get('free_seats'))
        model.save()
        return redirect('/carrier_flights/')
    else:
        return render(request, 'carrier_flight_add.html', {'type': 'carrier_flight', 'carriers': Carriers.objects.all(), 'aircraft_types': AircraftType.objects.all()})


@csrf_exempt
def edit_carrier_flight(request, id: int):
    if request.method == 'POST':
        model = CarrierFlights.objects.get(id=id)
        model.id_carrier = int(request.POST.get('id_carrier')) or None
        model.numb_flight = int(request.POST.get('numb_flight'))
        model.date_f = datetime.fromisoformat(request.POST.get('date_f')) if request.POST.get('date_f') else datetime.fromisoformat('2022-01-01')
        model.id_aircraft_type = int(request.POST.get('id_aircraft_type')) or None
        model.free_seats = int(request.POST.get('free_seats'))
        model.save()
        return redirect('/carrier_flights/')
    else:
        return render(request, 'carrier_flight_edit.html', {'type': 'carrier_flight', 'model': CarrierFlights.objects.get(id=id), 'carriers': Carriers.objects.all(), 'aircraft_types': AircraftType.objects.all()})


@csrf_exempt
def delete_carrier_flight(request, id: int):
    model = CarrierFlights.objects.get(id=id)
    model.delete()
    return redirect('/carrier_flights/')


def clients(request):
    return render(request, 'model_list.html', {'name': 'client', 'models': Clients.objects.all()})


@csrf_exempt
def add_client(request):
    if request.method == 'POST':
        model = Clients()
        model.s_name = request.POST.get('s_name')
        model.f_name = request.POST.get('f_name')
        model.t_name = request.POST.get('t_name')
        model.phone = request.POST.get('phone')
        model.save()
        return redirect('/clients/')
    else:
        return render(request, 'client_add.html', {'type': 'client'})


@csrf_exempt
def edit_client(request, id: int):
    if request.method == 'POST':
        model = Clients.objects.get(id=id)
        model.s_name = request.POST.get('s_name')
        model.f_name = request.POST.get('f_name')
        model.t_name = request.POST.get('t_name')
        model.phone = request.POST.get('phone')
        model.save()
        return redirect('/clients/')
    else:
        return render(request, 'client_edit.html', {'type': 'client', 'model': Clients.objects.get(id=id)})


@csrf_exempt
def delete_client(request, id: int):
    model = Clients.objects.get(id=id)
    model.delete()
    return redirect('/clients/')


def client_orders(request):
    return render(request, 'client_order_list.html', {'name': 'client_order', 'models': ClientOrders.objects.filter(date_order__gt=(datetime.now() - timedelta(days=365))).all()})


@csrf_exempt
def add_client_order(request):
    if request.method == 'POST':
        model = ClientOrders()
        model.client_model = Clients.objects.filter(id=int(request.POST.get('id_client'))).first() if int(request.POST.get('id_client')) else None
        model.date_order = datetime.fromisoformat(request.POST.get('date_order')) if request.POST.get('date_order') else datetime.fromisoformat('2022-01-01')
        model.id_order_type = int(request.POST.get('id_order_type')) or None
        model.save()
        return redirect('/client_orders/')
    else:
        return render(request, 'client_order_add.html', {'type': 'client_order', 'clients': Clients.objects.all(), 'order_types': OrderType.objects.all()})


@csrf_exempt
def edit_client_order(request, id: int):
    if request.method == 'POST':
        model = ClientOrders.objects.get(id=id)
        model.client_model = Clients.objects.filter(id=int(request.POST.get('id_client'))).first() if int(request.POST.get('id_client')) else None
        model.date_order = datetime.fromisoformat(request.POST.get('date_order')) if request.POST.get(
            'date_order') else datetime.fromisoformat('2022-01-01')
        model.id_order_type = int(request.POST.get('id_order_type')) or None
        model.save()
        return redirect('/client_orders/')
    else:
        return render(request, 'client_order_edit.html', {'type': 'client_order', 'model': ClientOrders.objects.get(id=id), 'clients': Clients.objects.all(), 'order_types': OrderType.objects.all()})


@csrf_exempt
def bill_client_order(request, id: int):
    if request.method == 'POST':
        model = ClientOrders.objects.get(id=id)
        model.id_client = int(request.POST.get('id_client')) or None
        model.date_order = datetime.fromisoformat(request.POST.get('date_order')) if request.POST.get(
            'date_order') else datetime.fromisoformat('2022-01-01')
        model.save()
        return redirect('/client_orders/')
    else:
        return render(request, 'client_order_bill.html', {'type': 'client_order', 'model': ClientOrders.objects.get(id=id), 'clients': Clients.objects.all()})


@csrf_exempt
def delete_client_order(request, id: int):
    model = ClientOrders.objects.get(id=id)
    model.delete()
    return redirect('/client_orders/')


def client_tours(request):
    return render(request, 'client_tour_list.html', {'name': 'client_tour', 'models': ClientTours.objects.all()})


@csrf_exempt
def add_client_tour(request):
    if request.method == 'POST':
        model = ClientTours()
        model.id_routes = int(request.POST.get('id_routes')) or None
        model.id_client_orders = int(request.POST.get('id_client_orders')) or None
        model.id_carrier_flights = int(request.POST.get('id_carrier_flights')) or None
        model.seat = request.POST.get('seat')
        model.save()
        return redirect('/client_tours/')
    else:
        return render(request, 'client_tour_add.html', {'type': 'client_tour', 'routes': Routes.objects.all(), 'client_orders': ClientOrders.objects.all(), 'carrier_flights': CarrierFlights.objects.all()})


@csrf_exempt
def edit_client_tour(request, id: int):
    if request.method == 'POST':
        model = ClientTours.objects.get(id=id)
        model.id_routes = int(request.POST.get('id_routes')) or None
        model.id_client_orders = int(request.POST.get('id_client_orders')) or None
        model.id_carrier_flights = int(request.POST.get('id_carrier_flights')) or None
        model.seat = request.POST.get('seat')
        model.save()
        return redirect('/client_tours/')
    else:
        return render(request, 'client_tour_edit.html', {'type': 'client_tour', 'model': ClientTours.objects.get(id=id), 'routes': Routes.objects.all(), 'client_orders': ClientOrders.objects.all(), 'carrier_flights': CarrierFlights.objects.all()})


@csrf_exempt
def delete_client_tour(request, id: int):
    model = ClientTours.objects.get(id=id)
    model.delete()
    return redirect('/client_tours/')


def main(request):
    return render(request, 'mainpage.html')