# -*- coding:UTF-8 -*-
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Identity, MapCompose


class MtimeLoader(ItemLoader):

    default_output_processor = TakeFirst()


    image_urls_out = Identity()

    title_in = MapCompose(str.strip)

    director_in = MapCompose(str.strip)
    director_out = Join('/')

    actors_in = MapCompose(str.strip)
    actors_out = Join('/')

    categories_in = MapCompose(str.strip)
    categories_out = Join('/')

    description_in = MapCompose(str.strip)

    points_in = MapCompose(str.strip)
    points_out = Join('')
