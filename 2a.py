import pandas as pd

# Nạp dữ liệu
df = pd.read_csv('IMDB-Movie-Data.csv')

# A. Xử lý dữ liệu cơ bản

# a. Hiển thị 5 dòng đầu tiên
print("5 dòng đầu tiên của dữ liệu:")
print(df.head(5))

# b. Thông tin chi tiết về dữ liệu
print("\nThông tin chi tiết của dữ liệu:")
print(df.info())

# c. Thống kê tổng quan về dữ liệu
print("\nThống kê tổng quan về dữ liệu:")
print(df.describe())

# d. Lấy các cột Title, Genre, Rating, Votes
df_selected = df[['Title', 'Genre', 'Rating', 'Votes']]
print("\nDữ liệu các cột Title, Genre, Rating, Votes:")
print(df_selected.head())

# e. Kiểm tra số lượng giá trị null
null_counts = df.isnull().sum()
print("\nSố lượng giá trị null trong từng cột:")
print(null_counts)

# f. Thay thế giá trị null trong cột Revenue bằng giá trị trung bình
df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean())

# g. Kiểm tra và loại bỏ dữ liệu trùng lặp
duplicate_count = df.duplicated().sum()
print(f"\nSố lượng dữ liệu trùng lặp: {duplicate_count}")
df.drop_duplicates(inplace=True)

# B. Phân tích dữ liệu

# a. Lấy các bộ phim từ 2010-2015, rating < 6.0, có doanh thu cao nhất
filtered_movies = df[(df['Year'] >= 2010) & (df['Year'] <= 2015) & (df['Rating'] < 6.0)]
top_revenue_movie = filtered_movies.loc[filtered_movies['Revenue (Millions)'].idxmax()]
print("\nBộ phim từ 2010-2015, rating < 6.0, có doanh thu cao nhất:")
print(top_revenue_movie)

# b. Lấy các bộ phim thuộc thể loại "Action"
action_movies = df[df['Genre'].str.contains('Action', na=False)]
print("\nCác bộ phim thuộc thể loại 'Action':")
print(action_movies)

# c. Lấy 5 bộ phim có lượt vote cao nhất
top_voted_movies = df.nlargest(5, 'Votes')
print("\n5 bộ phim có lượt vote cao nhất:")
print(top_voted_movies)

# d. Tính số rating trung bình của từng đạo diễn
director_avg_rating = df.groupby('Director')['Rating'].mean()
print("\nRating trung bình của từng đạo diễn:")
print(director_avg_rating)

# e. Tạo cột phân loại Rating: "Good", "Average", "Bad"
def categorize_rating(rating):
    """Phân loại rating thành Good, Average, Bad."""
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'

df['Rating_Category'] = df['Rating'].apply(categorize_rating)
print("\nDữ liệu với cột phân loại Rating:")
print(df[['Title', 'Rating', 'Rating_Category']].head(20))

# f. Tính tổng doanh thu của từng đạo diễn
director_revenue_sum = df.groupby('Director')['Revenue (Millions)'].sum()
print("\nTổng doanh thu của từng đạo diễn:")
print(director_revenue_sum)