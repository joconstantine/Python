from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "vo-de-6",
        "image": "mountains.jpg",
        "author": "Jo Constantine",
        "date": date(2019, 1, 24),
        "title": "Vô Đề 6",
        "excepts": "Xin đời là thảm cỏ\nTa nằm chết hồn nhiên\nTrời sang mùa nắng đỏ\nPhượng vĩ chắp tay thiền",
        "content": """
            Xin đời là thảm cỏ
            Ta nằm chết hồn nhiên
            Trời sang mùa nắng đỏ
            Phượng vĩ chắp tay thiền

            Gió cao nguyên ào ạt
            Hàng thông reo vi vu
            Như tiếng kinh hoan lạc
            Tiễn người vào thiên thu

            Bụi đời vương gót chân
            Mấy kiếp vẫn phong trần
            Mây tím cười nghiêng ngả
            Phù vân hỡi phù vân!

            Chim chóc lời cao thượng
            Tiếng thanh bôi ngọt ngào
            Giữa trầm luân vô vọng
            Vẫn ước phần thanh cao

            Ta nằm đó hồn nhiên
            Trên thảm cỏ xanh huyền
            Bao điêu linh xin hãy
            Tha đời này bình yên.
                        """,
    },
    {
        "slug": "doi-vang",
        "image": "coding.jpg",
        "author": "Jo Constantine",
        "date": date(2019, 1, 24),
        "title": "Đồi vắng",
        "excepts": """
            Đưa em lên đồi vắng
            Một buổi chiều thiết tha
            Em ngập ngừng lên mắt
            Mờ trong giọt nước ngà.
        """,
        "content": """
            Đưa em lên đồi vắng
            Một buổi chiều thiết tha
            Em ngập ngừng lên mắt
            Mờ trong giọt nước ngà.

            Tay em từng ngón tay
            Vòng ôm đôi vai gầy
            Gió nhẹ nhàng vê áo
            Vạt cuối trời mây bay

            Em ngập ngừng: Anh nhé!
            Chuyện xưa xa lắm rồi
            Thuyền giờ đanh đã đóng
            Tiếc thương cũng thế thôi.

            Thân em run trong nắng
            Từng vạt trắng cuối ngày
            Từng nhịp tim vô tận
            Từng giờ phút đắng cay

            Cỏ hồng rạp muôn lối
            Hoa tươi héo úa tàn
            Níu được sao bước vội
            Của một người sang ngang?

            Em rồi về bên ấy
            Ta vẫn đứng ngập ngừng
            Nhặt trong chiều cô lẻ
            Ân ái lẫn niềm thương.

            Đưa em lên đồi vắng
            Để nghe tiếc thương mình
            Đêm buông màn hoang lạnh
            Che khuất cả bình minh.
        """,
    },
    {
        "slug": "biet-san-ga",
        "image": "woods.jpg",
        "author": "Jo Constantine",
        "date": date(2019, 1, 24),
        "title": "Biệt Sân Ga",
        "excepts": """
            Người đi rồi giữa đêm vắng buồn tênh
            Sân ga nhỏ đường tàu không chạy quanh
        """,
        "content": """
            Người đi rồi giữa đêm vắng buồn tênh
            Sân ga nhỏ đường tàu không chạy quanh
            Gót bâng khuâng, hỏi lòng buồn không hở?
            Ngày xa dần, như hạnh phúc mong manh.

            Người đi rồi, ai nhặt nỗi nhớ nhung
            Để rơi nát những mơ ước tương phùng
            Đêm cuối cùng gần nhau trong sợ hãi
            Tương lai dài biết đâu chuyện cát hung.

            Người đi rồi, sương lạnh lẽo đan vây
            Mờ hắt hiu đèn khuya soi bóng gầy
            Tôi lê bước kéo thân trong mộng ảo
            Hỏi nhân gian địa giới hay tù đày?

            Người ra đi chiều nay hay đêm mai?
            Người sắp đi hay người đã đi rồi?
            Có khi người hóa thành từng cơn đắng
            Hơi men nồng rượu tàn rung trên môi.
        """,
    },
]


def get_date(post):
    return post.get('date')

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    identified_post = next(
        post for post in all_posts if post.get('slug') == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
    })
