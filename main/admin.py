from django.contrib import admin
from .models import Banner,Category,Brand,Color,Size,Product,ProductAttribute,CartOrder,CartOrderItems,ProductReview,Wishlist,UserAddressBook,PageVisit

# Register your models here.
admin.site.register(Brand)
admin.site.register(Size)



class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','brand','status','is_featured')
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)


class ProductAtrributeAdmin(admin.ModelAdmin):
    list_display = ('id','product','color','size','price','image')
admin.site.register(ProductAttribute,ProductAtrributeAdmin)



# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)


admin.site.register(Wishlist)


class UserAddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
admin.site.register(UserAddressBook,UserAddressBookAdmin)



class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'path', 'visit_count', 'last_visit')
    
admin.site.register(PageVisit, PageVisitAdmin)
