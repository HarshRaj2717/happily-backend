# happily-backend

Backend APIs for the Happily project by Moon And Stars team.

## Production Settings

- Add the following fields to `.env` file at root folder:
  ```
  django_secret_key=""
  happily_sender_email=""
  happily_sender_email_password=""
  DJANGO_SUPERUSER_USERNAME=""
  DJANGO_SUPERUSER_EMAIL=""
  DJANGO_SUPERUSER_PASSWORD=""
  WEB_CONCURRENCY=
  frontend_secret_key=""
  neon_db_username=""
  neon_db_password=""
  neon_db_host=""
  neon_db_port=""
  ```

## API Usage

- base link: https://happily-backend.onrender.com
- frontend_api_key: ... (api key needed to call this API)
- user_api_key: ... (given in response to successful & verified register/login API calls, unique for every user)

### authentication

- link: `base_link/frontend_api_key/auth/register`
- create user example: `base_link/frontend_api_key/auth/register/?email=example@example.com&password=1234`
- code verify example: `base_link/frontend_api_key/auth/register/?email=example@example.com&code=633025`

- link: `base_link/frontend_api_key/auth/login`
- login example: `base_link/frontend_api_key/auth/login/?email=example@example.com&password=1234`

### scales

- link: `base_link/frontend_api_key/scales`
- all scales: `base_link/frontend_api_key/scales`
- scale example: `base_link/frontend_api_key/scales/gidyq-aa-female/`
- user res: `base_link/frontend_api_key/scales/gidyq-aa-female/?user_res=1,3,2,0,2,0`

### community

- get all available posts - `base_link/frontend_api_key/get-posts/`
- get comments of a specific post - `base_link/frontend_api_key/get-comments/post_id (eg: base_link/frontend_api_key/get-comments/1)`
- create a post (user api key needed) - `base_link/frontend_api_key/user_api_key/create-post`
- delete a post (user api key needed) - `base_link/frontend_api_key/user_api_key/delete-post/post_id (eg: base_link/frontend_api_key/user_api_key/delete-post/1)`
- create a comment to a post (user api key needed) - `base_link/frontend_api_key/user_api_key/create-comment/post_id (eg: base_link/frontend_api_key/user_api_key/create-comment/1)`
- create a comment to a post (user api key needed) - `base_link/frontend_api_key/user_api_key/delete-comment/post_id/comment_id (eg: base_link/frontend_api_key/user_api_key/delete-comment/1/1)`
- upvote/like a post (user api key needed) - `base_link/frontend_api_key/user_api_key/upvote-post/post_id (eg: base_link/frontend_api_key/user_api_key/upvote-post/1)`
- downvote/dislike a post (user api key needed) - `base_link/frontend_api_key/user_api_key/downvote-post/post_id (eg: base_link/frontend_api_key/user_api_key/downvote-post/1)`
