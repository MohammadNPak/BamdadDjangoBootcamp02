from django.contrib.auth import get_user_model
from django.db.models import Max
from django.shortcuts import get_object_or_404

from problems.models import Submission, Problem
from .models import Contest

User = get_user_model()


def list_problems(contest_id):
    return Contest.objects.get(id=contest_id).problems.all()


def list_users(contest_id):
    return Contest.objects.get(id=contest_id).participants.all()


def list_submissions(contest_id):
    return Submission.objects.filter(problem__contest__id=contest_id).order_by("-submitted_time")


def list_problem_submissions(contest_id, problem_id):
    return Submission.objects.filter(problem__id=problem_id,problem__contest__id=contest_id).order_by("-submitted_time")


def list_user_submissions(contest_id, user_id):
    return Submission.objects.filter(problem__contest__id=contest_id,participant__id=user_id).order_by("-submitted_time")


def list_problem_user_submissions(contest_id, user_id, problem_id):
    return Submission.objects.filter(problem__id=problem_id,problem__contest__id=contest_id,participant__id=user_id).order_by("-submitted_time")


def list_users_solved_problem(contest_id, problem_id):
    return User.objects.filter(submissions__problem__id=problem_id,submissions__problem__contest__id=contest_id,submissions__score=F("submissions__problem__score")).order_by("-submissions__submitted_time")


    #     return User.objects.filter(
    #     participants__id=contest_id,
    #     submissions__problem__id=problem_id,
    #     participants__problems=problem_id,
    #     submissions__score=F("submissions__problem__score")
    # ).order_by("-submissions__submitted_time")



def user_score(contest_id, user_id):
    pass


def list_final_submissions(contest_id):
    pass

