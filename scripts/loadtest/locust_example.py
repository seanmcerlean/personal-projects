#!/usr/bin/python

"""
Example locustio script to test a web API
* Get, Post and Put requests
* Demonstrates weighted traffic including nested traffic flows
* Demonstrates rolling up of statistics using name
* uses faker and random libraries ot generate fake data

Targeted at http://jsonplaceholder.typicode.com/ for an example - D/L a locla version if high load desired

"""

from faker import Factory
from random import randint
from locust import HttpLocust, TaskSet, task


class CommentGenerator():
    def __init__(self):
        self.fake = Factory.create('EN_GB')

    def id(self):
        return str(randint(1, 100))

    def comment(self):
        data = {
            'title': self.fake.name(),
            'body':  self.fake.text(),
            'userId': str(randint(1, 100))
        }
        return data


class GetSite(TaskSet):
    _generator = CommentGenerator()

    @task(5)
    def get_post(self):
       id = self._generator.id()
       self.client.get('posts/' + id, name='/posts/[id]')

    @task(1)
    def get_post_comments(self):
        id = self._generator.id()
        self.client.get('comments', params={'postId': id}, name='/comments?postId=[id]')

    @task(3)
    def stop(self):
        self.interrupt()


class UpdateSite(TaskSet):
    _generator = CommentGenerator()

    @task(2)
    def add_post(self):
        comment = self._generator.comment()
        self.client.post('posts/', data=comment)

    @task(3)
    def update_post(self):
        comment = self._generator.comment()
        comment['id'] = self._generator.id()
        self.client.put('posts/' + comment['id'], data=comment, name='/posts/[id]')

    @task(1)
    def stop(self):
        self.interrupt()


class UserBehaviour(TaskSet):
    tasks = {GetSite: 3, UpdateSite: 1}


class APIUser(HttpLocust):
    task_set = UserBehaviour
    min_wait=5000
    max_wait=9000