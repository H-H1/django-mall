import xadmin
from goods.models import Brand, GoodsCategory, Goods, GoodsSpecification, SpecificationOption, SKU, \
    SKUSpecification, SKUImage

xadmin.site.register(Brand)
xadmin.site.register(GoodsCategory)
xadmin.site.register(Goods)
xadmin.site.register(GoodsSpecification)
xadmin.site.register(SpecificationOption)
xadmin.site.register(SKU)
xadmin.site.register(SKUImage)
xadmin.site.register(SKUSpecification)