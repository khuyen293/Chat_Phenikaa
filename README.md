
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

# Chatbot Phenikaa

## Mô tả: 
Chatbot Phenikaa là ứng dụng cho phép người dùng có thể tra cứu thông tin, tương tác với chatbot tự động.   

Mục tiêu của dự án là tạo ra một hệ thống chatbot linh hoạt và thông minh, nhằm cung cấp dịch vụ hỗ trợ và thông tin đa dạng, từ thông tin về chương trình học tập đến các thông báo sự kiện và tư vấn về dịch vụ sinh viên.    
  
Chúng tôi cũng cung cấp giao diện trực quan, giúp người dùng có thể dễ dàng thao tác với ứng dụng.

## Giao diện minh họa 
![Ảnh chụp màn hình 2023-11-16 075552](https://github.com/khuyen293/Undefined/assets/94832743/9458648e-a23b-4c2f-b5b0-6785af27c6a9)

## Phạm vi:
Ứng dụng web chatbot có thể truy cập bởi bất kỳ ai muốn tìm hiểu thông tin về trường, nếu là sinh viên hay cán bộ, giảng viên, nhân viên của trường thì có thể hỏi về các quy chế, quy định và hoạt động của trường thông qua tài liệu PDF được tải lên bởi admin

**Tính khả dụng**: Hệ thống dễ dàng tương tác và xử lý tác vụ, giao diện thân thiện, dễ sử dụng. Xử lý ngôn ngữ tự nhiên tốt.

**Tính tin cậy**: Hệ thống có thể sử dụng mọi lúc, đáp ứng tần suất truy cập cao.

**Tính bảo mật**: Hệ thống mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu, đảm bảo sẽ không bị lộ mật khẩu nếu cơ sở dữ liệu bị lấy cắp.

**Ràng buộc thiết kế**: Hệ thống cung cấp giao diện chủ yếu cho màn hình máy tính, giao diện thân thiện, dễ sử dụng. 

## Các công nghệ được sử dụng: 
    
**Flask** : Flask là một khung ứng dụng web WSGI nhẹ. Nó được thiết kế để giúp bắt đầu nhanh chóng và dễ dàng, với khả năng mở rộng quy mô cho các ứng dụng phức tạp. Nó bắt đầu như một trình bao bọc đơn giản xung quanh Werkzeug và Jinja và đã trở thành một trong những khung ứng dụng web Python phổ biến nhất.

**Flask** đưa ra các đề xuất nhưng không thực thi bất kỳ sự phụ thuộc hoặc bố cục dự án nào. Nhà phát triển có quyền lựa chọn các công cụ và thư viện mà họ muốn sử dụng. Có nhiều tiện ích mở rộng được cộng đồng cung cấp giúp việc thêm chức năng mới trở nên dễ dàng.

**🦜️🔗 LangChain** : Langchain là một mạng neural kết nối ngôn ngữ không gian-thời gian, được phát triển bởi Google AI vào năm 2022. Nó được thiết kế để hiểu và tạo ra văn bản, đồng thời học các mô hình ngôn ngữ phức tạp. Langchain hoạt động bằng cách chia văn bản thành các đoạn nhỏ, mỗi đoạn được đại diện bởi một vector. Các vector này sau đó được kết nối với nhau bằng các trọng số, tạo thành một mạng neural. Mạng neural này có thể học các mô hình ngôn ngữ phức tạp bằng cách phân tích văn bản.

## Mô hình hệ thống
   ![Structure](https://github.com/khuyen293/Undefined/assets/96828322/d671e71b-48c1-4223-b026-30b2f4371ef8)

   Hệ thống gồm 2 phân quyền dữ liệu chính:  
    - Người dùng không sử dụng tài khoản email của trường sẽ bị giới hạn nội dung tìm kiếm (không thể truy cập những tài liệu PDF của trường gửi cho sinh viên).  
    - Người dùng có sử dụng tài khoản có thể truy tra cứu, tìm kiếm với nội dung nội bộ
   Input và output có thể được xử lí qua định dạng voice và text
  
## Hướng dẫn sử dụng
1. Clone my repo:  
``` git clone https://github.com/khuyen293/Undefined ```
2. Thêm file .env vào thư mục gốc  
3. Thêm biến OPENAI_API_KEY     
   ``` OPENAI_API_KEY = "sk - ..." ```
4. Install các thư viện cần thiết  
   ``` pip install -r requirements ```
5. Chạy chương trình  
   ``` python run.py```


## Tính năng
- [x] Chat with GPT-3.5
- [x] Easy to operate

