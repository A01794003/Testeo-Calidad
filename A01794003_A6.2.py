import csv
import os
import unittest
import coverage

class Hotel:
    def __init__(self, hotel_id, name, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms_available = rooms_available

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Reservation:
    def __init__(self, reservation_id, customer, hotel, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

class ReservationSystem:
    def __init__(self):
        self.hotels = []
        self.customers = []
        self.reservations = []

    def create_hotel(self, hotel_id, name, rooms_available):
        hotel = Hotel(hotel_id, name, rooms_available)
        self.hotels.append(hotel)
        self.save_hotels_to_csv()

    def delete_hotel(self, hotel_id):
        self.hotels = [hotel for hotel in self.hotels if hotel.hotel_id != hotel_id]
        self.save_hotels_to_csv()

    def display_hotel_info(self, hotel_id):
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                print(f"Hotel ID: {hotel.hotel_id}")
                print(f"Name: {hotel.name}")
                print(f"Rooms Available: {hotel.rooms_available}")
                break
        else:
            print("Hotel not found.")

    def modify_hotel_info(self, hotel_id, new_name, new_rooms_available):
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                hotel.name = new_name
                hotel.rooms_available = new_rooms_available
                self.save_hotels_to_csv()
                break
        else:
            print("Hotel not found.")

    def reserve_room(self, customer_id, hotel_id, check_in_date, check_out_date):
        customer = next((c for c in self.customers if c.customer_id == customer_id), None)
        hotel = next((h for h in self.hotels if h.hotel_id == hotel_id), None)
        if customer and hotel:
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(reservation_id, customer, hotel, check_in_date, check_out_date)
            self.reservations.append(reservation)
            print(f"Reservation created with ID: {reservation_id}")
        else:
            print("Customer or hotel not found.")

    def save_hotels_to_csv(self):
        with open("hotels.csv", "w", newline="") as csvfile:
            fieldnames = ["hotel_id", "name", "rooms_available"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for hotel in self.hotels:
                writer.writerow({"hotel_id": hotel.hotel_id, "name": hotel.name, "rooms_available": hotel.rooms_available})

# Example usage:
system = ReservationSystem()
system.create_hotel(1, "Hotel A", 50)
system.create_hotel(2, "Hotel B", 30)
system.display_hotel_info(1)
system.modify_hotel_info(1, "New Hotel A", 60)
system.reserve_room(1, 1, "2024-02-01", "2024-02-05")
