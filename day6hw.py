blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total_views = 0
trending_posts = 0


for views in blog_views:
    if views > 1000:
        print("Trending")
        trending_posts += 1
    elif   500 <= views <= 1000:
        print("Average")
    else:
        print("Low Traffic")
    total_views += views


print("Total views:", total_views)
print("Number of Trending posts:", trending_posts)