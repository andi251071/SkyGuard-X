# AUTOMATED BILLING SYSTEM 
from datetime import datetime, timedelta 
import json 
 
class BillingSystem: 
    def __init__(self): 
        self.invoices = {} 
        self.customers = {} 
        self.payment_gateways = { 
            'stripe': {'fee_percentage': 2.9, 'fixed_fee': 0.30}, 
            'paypal': {'fee_percentage': 3.5, 'fixed_fee': 0.35}, 
            'bank_transfer': {'fee_percentage': 0, 'fixed_fee': 0} 
        } 
 
    def create_invoice(self, customer_id, amount, description): 
        invoice_id = f"INV-{datetime.now().strftime('%Y%m%d')}-{len(self.invoices)+1:04d}" 
        due_date = datetime.now() + timedelta(days=30) 
 
        invoice = { 
            'invoice_id': invoice_id, 
            'customer_id': customer_id, 
            'amount': amount, 
            'description': description, 
            'created_date': datetime.now().isoformat(), 
            'due_date': due_date.isoformat(), 
            'status': 'pending' 
        } 
 
        self.invoices[invoice_id] = invoice 
        return invoice 
 
    def process_payment(self, invoice_id, payment_method, amount): 
        if invoice_id not in self.invoices: 
            return {'error': 'Invoice not found'} 
 
        invoice = self.invoices[invoice_id] 
 
        # Calculate payment gateway fees 
        gateway = self.payment_gateways.get(payment_method, self.payment_gateways['stripe']) 
        gateway_fee = (amount * gateway['fee_percentage'] / 100) + gateway['fixed_fee'] 
        net_amount = amount - gateway_fee 
 
        # Update invoice status 
        invoice['status'] = 'paid' 
        invoice['payment_date'] = datetime.now().isoformat() 
        invoice['payment_method'] = payment_method 
        invoice['gateway_fee'] = round(gateway_fee, 2) 
        invoice['net_amount'] = round(net_amount, 2) 
 
        return { 
            'success': True, 
            'invoice_id': invoice_id, 
            'amount_paid': amount, 
            'net_amount': net_amount, 
            'gateway_fee': gateway_fee 
        } 
 
    def get_revenue_report(self): 
        total_revenue = 0 
        total_fees = 0 
        paid_invoices = [inv for inv in self.invoices.values() if inv['status'] == 'paid'] 
 
        for invoice in paid_invoices: 
            total_revenue += invoice.get('net_amount', 0) 
            total_fees += invoice.get('gateway_fee', 0) 
 
        return { 
            'total_invoices': len(paid_invoices), 
            'total_revenue': round(total_revenue, 2), 
            'total_fees': round(total_fees, 2), 
            'net_income': round(total_revenue - total_fees, 2), 
            'report_date': datetime.now().isoformat() 
        } 
