from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Movie

class FavoriteMovieTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='watcher',password='0000')
        test_user.save()

        test_favorites = Movie.objects.create(
            name = 'Iron man',
            rate = 8.0,
            release = '2008-1-1',
            genre = 'Action',
            admin = test_user
        )
        test_favorites.save()
    
    def test_movies_content(self):
        fav = Movie.objects.get(id=1)

        self.assertEqual(str(fav.admin), 'watcher')
        self.assertEqual(fav.name, 'Iron man')
        self.assertEqual(fav.rate, 8.0)
        self.assertEqual(fav.genre, 'Action')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('favorite_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='watcher',password='0000')
        test_user.save()

        test_favorites = Movie.objects.create(
            name = 'Iron man',
            rate = 8.0,
            release = '2008-01-01',
            genre = 'Action',
            admin = test_user,
        )
        test_favorites.save()

        response = self.client.get(reverse('favorite_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'name':test_favorites.name,
            'rate':test_favorites.rate,
            'release': test_favorites.release,
            'genre':test_favorites.genre,
            'admin': test_favorites.id,
        })
    
    def test_create(self):
        test_user = get_user_model().objects.create_user(username='watcher',password='0000')
        test_user.save()

        url = reverse('favorite_list')
        data = {
            'name': 'Iron man',
            'rate': 8.0,
            'release': '2008-01-01',
            'genre': 'Action',
            'admin': test_user.id,
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)
        self.assertEqual(Movie.objects.count(),1)
        self.assertEqual(Movie.objects.get().name, data['name'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='watcher',password='0000')
        test_user.save()

        test_favorites = Movie.objects.create(
            name = 'Iron man',
            rate = 8.0,
            release = '2008-01-01',
            genre = 'Action',
            admin = test_user,
        )
        test_favorites.save()

        url = reverse('favorite_detail', args=[test_user.id])
        data = {
            'name': 'Iron man',
            'rate': 8.0,
            'release': '2008-01-01',
            'genre': 'Action',
            'admin': test_user.id,
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Movie.objects.count(), test_user.id)
        self.assertEqual(Movie.objects.get().name, data['name'])
    
    def test_delete(self):
        test_user = get_user_model().objects.create_user(username='watcher',password='0000')
        test_user.save()

        test_favorites = Movie.objects.create(
        name = 'Iron man',
        rate = 8.0,
        release = '2008-1-1',
        genre = 'Action',
        admin = test_user
        )
        test_favorites.save()

        fav = Movie.objects.get()
        url = reverse('favorite_detail', kwargs={'pk': fav.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, url)