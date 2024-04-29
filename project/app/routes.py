from flask import Flask, Blueprint
import csv
import json
import os
import app.func as func
from flask import jsonify

txn_app = Blueprint("txn_app", __name__)

@txn_app.route("/transaction")
def home():
   return func.read_csv('transaction', True).to_json(orient='records')

@txn_app.route("/product")
def product():
   return func.read_csv('reference', False).to_json(orient='records')

@txn_app.route("/assignment/<int:transaction_id>")
def assignment_transaction_id(transaction_id):
   return func.get_transactionId(transaction_id).to_json(orient='records')

@txn_app.route("/assignment/getTransactionSummaryByProducts/<int:last_n_days>")
def getTransactionSummaryByProducts(last_n_days):
   return func.transaction_products(last_n_days, 'productName').to_json(orient='records')

@txn_app.route("/assignment/getTransactionSummaryByManufacturingCity/<int:last_n_days>")
def getTransactionSummaryByManufacturingCity(last_n_days):
   return func.transaction_products(last_n_days, 'productManufacturingCity').to_json(orient='records')
