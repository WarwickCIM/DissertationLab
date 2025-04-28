# This script contains a basic recipe to scrape content from a website using
# {rvest} package. For illustrative purposes we will be scrapping this page with
# ratings from a tv show. Please note that IMBDB has an API that would be more
# suited for this task.



# Setup ------------------------------------------------------------------

# Uncomment below to install rvest if not ready installed.
# install.packages("rvest")

library(rvest)


# This is the url to scrape
url <- "https://www.imdb.com/title/tt31806037/reviews/?ref_=tt_ururv_sm"

# Retrieve the title of the page.
movie_title <- read_html(url) |> 
  html_element("h2") |> 
  html_text()

# Retrieve all reviews
reviews <- read_html(url) |> 
  html_elements("article") 

# Retrieve reviews' ratings.
ratings <- reviews |> 
  html_element(".ipc-rating-star--rating") |> 
  html_text()

# Retrieve reviews' title
titles <- reviews |> 
  html_element("h3") |> 
  html_text()

# Extract reviews' URL
titles_link <- reviews |> 
  html_element(".ipc-title a") |> 
  html_attr("href")

# Extract the actual review.
text <- reviews |> 
  html_element(".ipc-html-content-inner-div") |> 
  html_text()



# Build a dataframe -------------------------------------------------------

reviews_df <- data.frame(
  titles, 
  titles_link,
  text,
  ratings 
)

reviews_df$movie <- movie_title

# The urls are relative to the scrapped page, so we can 
reviews_df$titles_link <- paste0(url, reviews_df$titles_link)

View(reviews_df)
