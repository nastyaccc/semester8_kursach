from django.urls import path

from . import views

urlpatterns = [
    path('positions/', views.positions),
    path('position/add/', views.add_position),
    path('position/edit/<int:id>', views.edit_position),
    path('position/delete/<int:id>', views.delete_position),

    path('reasons_for_transfer/', views.reasons_for_transfer),
    path('reason_for_transfer/add/', views.add_reason_for_transfer),
    path('reason_for_transfer/edit/<int:id>', views.edit_reason_for_transfer),
    path('reason_for_transfer/delete/<int:id>', views.delete_reason_for_transfer),

    path('countries/', views.countries),
    path('country/add/', views.add_country),
    path('country/edit/<int:id>', views.edit_country),
    path('country/delete/<int:id>', views.delete_country),

    path('cities/', views.cities),
    path('city/add/', views.add_city),
    path('city/edit/<int:id>', views.edit_city),
    path('city/delete/<int:id>', views.delete_city),

    path('hotel_types/', views.hotel_types),
    path('hotel_type/add/', views.add_hotel_type),
    path('hotel_type/edit/<int:id>', views.edit_hotel_type),
    path('hotel_type/delete/<int:id>', views.delete_hotel_type),

    path('carriers/', views.carriers),
    path('carrier/add/', views.add_carrier),
    path('carrier/edit/<int:id>', views.edit_carrier),
    path('carrier/delete/<int:id>', views.delete_carrier),

    path('aircraft_types/', views.aircraft_types),
    path('aircraft_type/add/', views.add_aircraft_type),
    path('aircraft_type/edit/<int:id>', views.edit_aircraft_type),
    path('aircraft_type/delete/<int:id>', views.delete_aircraft_type),

    path('order_types/', views.order_types),
    path('order_type/add/', views.add_order_type),
    path('order_type/edit/<int:id>', views.edit_order_type),
    path('order_type/delete/<int:id>', views.delete_order_type),

    path('employees/', views.employees),
    path('employee/add/', views.add_employee),
    path('employee/edit/<int:id>', views.edit_employee),
    path('employee/delete/<int:id>', views.delete_employee),

    path('employee_motions/', views.employee_motions),
    path('employee_motion/add/', views.add_employee_motion),
    path('employee_motion/edit/<int:id>', views.edit_employee_motion),
    path('employee_motion/delete/<int:id>', views.delete_employee_motion),

    path('routes/', views.routes),
    path('route/add/', views.add_route),
    path('route/edit/<int:id>', views.edit_route),
    path('route/delete/<int:id>', views.delete_route),

    path('hotels/', views.hotels),
    path('hotel/add/', views.add_hotel),
    path('hotel/edit/<int:id>', views.edit_hotel),
    path('hotel/delete/<int:id>', views.delete_hotel),

    path('carrier_flights/', views.carrier_flights),
    path('carrier_flight/add/', views.add_carrier_flight),
    path('carrier_flight/edit/<int:id>', views.edit_carrier_flight),
    path('carrier_flight/delete/<int:id>', views.delete_carrier_flight),

    path('clients/', views.clients),
    path('client/add/', views.add_client),
    path('client/edit/<int:id>', views.edit_client),
    path('client/delete/<int:id>', views.delete_client),

    path('client_orders/', views.client_orders),
    path('client_order/add/', views.add_client_order),
    path('client_order/edit/<int:id>', views.edit_client_order),
    path('client_order/bill/<int:id>', views.bill_client_order),
    path('client_order/delete/<int:id>', views.delete_client_order),

    path('client_tours/', views.client_tours),
    path('client_tour/add/', views.add_client_tour),
    path('client_tour/edit/<int:id>', views.edit_client_tour),
    path('client_tour/delete/<int:id>', views.delete_client_tour),

    path('main/', views.main),
]
