#!/usr/bin/env python3

APPROVED_JOBS = [
    "Unknown",
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name="Unknown",job="Unknown"):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name="Invalid name"
        else:
            self.name=name.title()
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self.job="Invalid job"
        else:
            self.job=job
