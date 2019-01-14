#!/usr/bin/env python
# -*- coding: utf-8 -*-

from girder.models.model_base import AccessControlledModel


class PixelAnnotation(AccessControlledModel):
    def initialize(self):
        self.name = 'pixelAnnotation'
