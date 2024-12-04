import pandas as pd

# 1. Hàm nạp dữ liệu và hiển thị 10 dòng đầu tiên
def load_and_display_data(file_path):
    """Nạp dữ liệu từ tệp CSV và hiển thị 10 dòng đầu tiên."""
    data = pd.read_csv(file_path)
    print("10 dòng dữ liệu đầu tiên:")
    print(data.head(10))
    return data

# Đường dẫn tệp CSV
file_path = 'xettuyendaihoc.csv'

# Nạp dữ liệu
data = load_and_display_data(file_path)

# 2. Kiểm tra kiểu dữ liệu của các trường
print("Các kiểu dữ liệu của các cột:")
print(data.dtypes)

# 3. Kiểm tra tổng số dữ liệu trống của các trường
missing_data_summary = data.isnull().sum()
print("Tổng dữ liệu trống của các trường:")
print(missing_data_summary)

# 4. Điền dữ liệu trống cột DT với giá trị 'K' và chuyển sang kiểu chuỗi
data['DT'] = data['DT'].fillna('K').astype(str)

# 5. Chuyển đổi dữ liệu khối thi thành mã số
exam_block_mapping = {'A': 0, 'A1': 1, 'B': 2, 'C': 3, 'D1': 46}
data['KT'] = data['KT'].map(exam_block_mapping)

# 6. Tạo cột tính điểm đại học và kết quả điểm sàn
data['Total_Score'] = data['DH1'] + data['DH2'] + data['DH3']
data['Result'] = data['Total_Score'].apply(lambda x: 'Đạt sàn' if x >= 15 else 'Không đạt sàn')

# Phần 2: Thống kê dữ liệu

# 1. Thống kê các chỉ số của DH1 theo khối thi (KT) và khu vực (KV)
dh1_stats = data.groupby(['KT', 'KV'])['DH1'].agg(['count', 'sum', 'mean', 'median', 'min', 'max'])
print("Thống kê DH1 theo KT và KV:")
print(dh1_stats)

# 2. Lọc dữ liệu thí sinh có DH1, DH2, DH3 >= 5 và thi khối A
filtered_candidates = data[(data['DH1'] >= 5) & (data['DH2'] >= 5) & (data['DH3'] >= 5) & (data['KT'] == 0)]
print("Thí sinh có điểm DH1, DH2, DH3 >= 5 và thi khối A:")
print(filtered_candidates)

# 3. Tính điểm trung bình 2 môn đầu tiên và điểm trung bình 3 môn
data['Average_DH1_DH2'] = (data['DH1'] + data['DH2']) / 2
data['Average_Total_Score'] = (data['DH1'] + data['DH2'] + data['DH3']) / 3
print("Điểm trung bình DH1, DH2 và điểm trung bình tổng:")
print(data[['Average_DH1_DH2', 'Average_Total_Score']])

# 4. Thống kê số lượng thí sinh Nam và Nữ theo dân tộc
gender_stats = data.groupby(['DT', 'GT'])['GT'].count().unstack(fill_value=0)
print("Số lượng thí sinh Nam và Nữ theo dân tộc:")
print(gender_stats)

# 5. Thống kê số lượng thí sinh từng khu vực theo khối thi
region_exam_block_stats = data.groupby(['KV', 'KT']).size().unstack(fill_value=0)
print("Số lượng thí sinh từng khu vực theo khối thi:")
print(region_exam_block_stats)

# 6. Thống kê số lượng thí sinh đậu, rớt trên từng khối thi
exam_block_result_stats = data.groupby(['KT', 'Result']).size().unstack(fill_value=0)
print("Số lượng thí sinh đậu/rớt theo khối thi:")
print(exam_block_result_stats)