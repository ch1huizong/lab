# -*- coding:UTF-8 -*-

import os

import falcon

import look.images


def create_app(image_store):
    api = falcon.API()
    api.add_route('/images', look.images.Collection(image_store))
    api.add_route('/images/{name}', look.images.Item(image_store))
    return api


def get_app():
    storage_path = os.environ.get('LOOK_STORAGE_PATH', '.')
    image_store = look.images.ImageStore(storage_path)
    return create_app(image_store)
