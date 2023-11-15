
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

# Chat Phenikaa

## Mô tả vấn đề:
Là những sinh viên khoa Công nghệ thông tin trường Đại học Phenikaa, chúng tôi đã được sử dụng rất nhiều tiện ích và công nghệ từ trường đại học của mình. Chúng tôi rất thích thú và tự hào, nhưng điều đó vô tình khiến lượng thông tin cần xử lí mỗi ngày đến rất nhiều và rời rạc với nhau. Đôi khi chúng tôi có thể bị quên và bỏ lỡ những thông tin quan trọng về lịch học, lịch nộp bài tập, sự kiện của trường, các thông báo về hành chính, … Điều đó ảnh hưởng trực tiếp tới kết quả học tập và trải nghiệm trong môi trường đại học không chỉ của chúng tôi mà còn của rất nhiều sinh viên khác trong trường.

## Giải pháp:
   Để tiết kiệm thời gian một cách tối đa và giúp cho người tìm kiếm có thể hiểu rõ ràng và chi tiết về một vấn đề liên quan đến nhà trường, chúng tôi đã lên ý tưởng và thực hiện việc xây dựng sản phẩm ChatPDF dành riêng cho trường đại học Phenikaa. Sản phẩm này sẽ giúp cho việc tìm kiếm những vấn đề liên quan đến trường đại học Phenikaa được trả lời một cách nhanh gọn, rõ ràng, chi tiết nhất có thể.

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



