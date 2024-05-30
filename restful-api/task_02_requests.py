import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])

    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:

          posts = response.json()

          data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

          fieldnames = ['id', 'title', 'body']

          with open('posts.csv', mode='w', newline='') as file:
              writer = csv.DictWriter(file, fieldnames=fieldnames)
              writer.writeheader()
              writer.writerows(data)

          print("Posts saved to posts.csv")
    else:
          print("Failed to fetch posts")

fetch_and_print_posts()
fetch_and_save_posts()
