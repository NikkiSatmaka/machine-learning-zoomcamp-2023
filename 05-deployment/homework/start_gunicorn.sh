#!/usr/bin/env bash
# -*- coding: utf-8 -*-

gunicorn --bind localhost:9696 predict_1:app
