# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 19:36:07 2026

@author: harish vijayarangan
"""

import random
from datetime import datetime, timedelta


def check_time(start, end):
    fmt = "%H:%M"

    slot_start = datetime.strptime(start, fmt)
    slot_end = datetime.strptime(end, fmt)
    now = datetime.now()

    # Set today's date
    slot_start = slot_start.replace(year=now.year, month=now.month, day=now.day)
    slot_end = slot_end.replace(year=now.year, month=now.month, day=now.day)

    grace_end = slot_end + timedelta(minutes=10)

    if now < slot_start:
        return "EARLY"
    elif slot_start <= now <= slot_end:
        return "ONTIME"
    elif slot_end < now <= grace_end:
        return "GRACE"
    else:
        return "EXPIRED"


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("Welcome to the Automated EV Charging Station!")

name = input("Enter your name: ")

start_time = input("Enter slot START time (HH:MM): ")
end_time = input("Enter slot END time (HH:MM): ")

print("\n--- Booking Details ---")
print("Name:", name)
print("Slot:", start_time, "to", end_time)
print("Booking Successful ")

# Generate OTP
otp = random.randint(100000, 999999)

print("\n Your OTP:", otp)
print("Please keep it safe.\n")

# OTP Verification
attempts = 3
verified = False

while attempts > 0:
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("OTP Verified ")
        verified = True
        break
    else:
        attempts -= 1
        print("Wrong OTP ")
        print("Attempts left:", attempts)

if not verified:
    print("\nToo many wrong attempts. Access Denied ")
    exit()

# Time Validation
status = check_time(start_time, end_time)

print("\n⏰ Time Status:", status)

if status == "EARLY":
    print("You arrived early. Please wait ")

elif status == "ONTIME":
    print("Charging Started ")

elif status == "GRACE":
    print("Within grace period. Charging Allowed ")

else:
    print("Slot expired. Booking cancelled ")
