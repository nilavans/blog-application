from models.user import User
from models.post import Post
from models.comment import Comment

class Manager:
   def __init__(self):
        self.current_user = None

   def get_choice(self, total_options):
       message = f"Enter your choice from 1 to {total_options}\n"
       choice = input(message)
       return int(choice)

   def print_menu(self):
       print('--------- BLOG MENU ----------')
       menu = [
            '1. Register',
            '2. Login',
            '3. Create posts',
            '4. View posts',
            '5. Add comment',
            '6. Exit'
            ]
       print('\n'.join(menu))
       print('--------------------------------')
       return self.get_choice(len(menu))
   
   def register(self):
      username = input('Username: ')
      email = input('Email: ')
      password = input('Password: ')
      role = input('Role (admin / author/ reader): ')
      user = User(username, email, password, role)
      if user.save(): 
         print('User registered successfully!')
      else:
         print('Registration failed, try again!')

   def login(self):
      username = input('Username: ')
      password = input('Password: ')
      user = User.authenticate(username, password)
      if user: 
         self.current_user = {'id': user[0], 'role': user[1]}
         print('Login successful!')
      else:
         print('Invalid credentials.')

   def create_post(self):
      if not self.current_user or self.current_user['role']!= 'author':
         print('Only authors can create posts.')
         return
      title = input('Title: ')
      category = input('Category: ')
      content = input('Content: ')
      post = Post(self.current_user['id'], title, category, content)
      if post.save():
         print('Post created successfully!')
      else:
         print('Failed to create post.')

   def view_posts(self):
      posts = Post.get_posts()
      print('------------------------------------------------------------------------')
      for post in posts:
         print(f'Post Id: {post[0]}, Title: {post[1]}, Category: {post[2]}, Date: {post[3]}')
      print('------------------------------------------------------------------------')

   
   def add_comment(self):
      if not self.current_user:
         print('Login to comment')
         return 
      
      post_id = int(input('Post ID: '))
      content = input('Comment: ')
      comment = Comment(post_id, self.current_user['id'], content)

      if comment.save():
         print('Comment added successfully!')
      else:
         print('Failed to add comment')

   def run(self):
        while True:
          choice = self.print_menu()
          
          if choice == 1:
            self.register()
          elif choice == 2:
             self.login()
          elif choice == 3:
             self.create_post()
          elif choice == 4:
             self.view_posts()
          elif choice == 5:
             self.add_comment()
          else:
             break