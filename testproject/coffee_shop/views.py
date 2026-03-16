from django.shortcuts import render

# Create your views here.

def index(request):
    header_p = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt inventore dolores perspiciatis."
    header_h1 = "The perfect world of coffee"

    section1_h2_span = "Дээд зэрэглэлийн кофег"
    section1_h2 = " хүн бүрт"
    section1_p = ['"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Temporibus porro inventore voluptatem ratione eum repellat quia et mollitia illum ut!"', 
                  '"Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestias voluptas, accusantium cupiditate a recusandae deserunt natus consectetur, rem quidem sint quae esse aspernatur nostrum quis?"', 
                  "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero neque est culpa! Dolores maiores veritatis, voluptatem earum magnam voluptate architecto vel facilis minima adipisci eius inventore necessitatibus nihil consequuntur dignissimos porro ad non ut obcaecati laborum sed suscipit. Tempora, aliquam."
                  ]
    
    section2_h2 = "Хамгийн шилдэг үйлчилгээг манайхаас"
    section2_button = "Цэс сонирхох"

    article_h2 = "Манай үйлчлүүлэгчдийн сэтгэгдлээс"
    article_detail = [{"text":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quaerat, fugiat dolores. A molestiae voluptatum, non mollitia doloremque ducimus ea numquam.",
                       "name":"John Doe",
                       "rating":"⭐⭐⭐⭐⭐"},
                       {"text":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quaerat, fugiat dolores. A molestiae voluptatum, non mollitia doloremque ducimus ea numquam. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellat, deleniti!",
                       "name":"Jane Doe",
                       "rating":"⭐⭐⭐⭐⭐"}]

    content = {
        "header_p": header_p,
        "header_h1": header_h1,
        "section1_h2_span": section1_h2_span,
        "section1_h2": section1_h2,
        "section1_p": section1_p,
        "section2_h2": section2_h2,
        "section2_button": section2_button,
        "article_h2": article_h2,
        "article_detail": article_detail
    }
    return render(request, "coffee_shop/index.html", content)

def menu(request):
    section_title = "Танд санал болгох цэс"
    section_contents = [
        {"name": "MOSCHA", "price": "9 500.00₮", "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit"},
        {"name": "ESPRESSO", "price": "9 900.00₮", "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit"},
        {"name": "AMERICANO", "price": "8 500.00₮", "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit"},
        {"name": "CAFE LATTE", "price": "9 600.00₮", "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit"},
        {"name": "FRAPPUCCINO", "price": "9 800.00₮", "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit"},
        {"name": "ICE COFFEE", "price": "8 800.00₮", "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit"}
    ]

    content = {
        "section_title": section_title,
        "section_contents": section_contents
    }
    return render(request, "coffee_shop/menu.html", content)

def about(request):
    section_contents = [{"num": "01", "title": "Алсын хараа", "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum quasi maiores, sapiente itaque provident error consequuntur. Cumque delectus voluptatem ea temporibus ipsa aut laudantium aspernatur!"}, 
                        {"num": "02", "title": "Зорилго", "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum quasi maiores, sapiente itaque provident error consequuntur. Cumque delectus voluptatem ea temporibus ipsa aut laudantium aspernatur! Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi laudantium tempore, nam eaque, voluptas corrupti laboriosam quasi aperiam inventore animi cupiditate! Totam delectus quas debitis obcaecati hic nostrum magnam reiciendis at enim iusto molestias, dolorum tempora consequatur odit. Quia, cumque excepturi dicta error sint alias ullam! Dolore, rem labore."}]
    
    section2_content = [{"h2": "Аз жаргалтай мөчийг", "h1": "кофеноос", "p": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum iste, veritatis qui enim nam ullam. Iusto, neque atque. Facilis natus culpa velit quidem voluptas repudiandae vitae corrupti est quas magni!"}]

    content = {
        "section_contents": section_contents,
        "section2_content": section2_content
    }
    return render(request, "coffee_shop/about.html", content)

def contact(request):
    address_info = [{"address": " Улаанбаатар хот", "phone": " 8866-2299", "email": " info@coffeeshop.mn"}]

    content = {
        "address_info": address_info
    }
    return render(request, "coffee_shop/contact.html", content)