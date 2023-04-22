from django.db import models


class Article(models.Model):
    link = models.CharField(max_length=4000)
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Actress(Article):
    pass


class Director(Article):
    pass


class Keyword(Article):
    pass


class Series(Article):
    pass


class Porn(models.Model):
    title = models.CharField(max_length=1000)
    delivery = models.DateField(null=True)
    release = models.DateField(null=True)
    duration = models.DurationField()
    actresses = models.ManyToManyField(Actress)
    # director = models.ForeignKey(Director)
    # self.series = self.get_series(soup)
    # self.maker = self.get_maker(soup)
    # self.label = self.get_label(soup)
    # self.rate = self.get_rate(soup)
    # self.package_image = self.get_package_image(soup, self.fanza_id)
    # self.package_image_thumbnail = self.get_package_image_thumbnail(soup, self.fanza_id)
    # self.sample_images = self.get_sample_images(soup)
    keywords = models.ManyToManyField(Keyword)
    fanza_id = models.CharField(max_length=100)
