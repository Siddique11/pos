from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'dashboards', DashboardViewSet)
router.register(r'product_categories', ProductCategoryViewSet)
router.register(r'product_brands', ProductBrandViewSet)
router.register(r'product_units', ProductUnitViewSet)
router.register(r'selling_price_groups', SellingPriceGroupViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_labels', ProductLabelViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sale_returns', SaleReturnViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'purchase_returns', PurchaseReturnViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'customer_groups', CustomerGroupViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'expense_categories', ExpenseCategoryViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'counters', CounterViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'profit_loss_reports', ProfitLossReportViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'cashiers', CashierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
