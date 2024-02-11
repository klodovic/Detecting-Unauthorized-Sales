from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sales', methods=['POST'])
def detectingUnAuthorizedSales():

    data = request.get_json() 
    response = ""
    
    #checking if data exists
    if not data:
        response = "Error - Not Acceptable"
        return jsonify(response), 406
    
    #checkin if data have lists
    for d in data:
        if d != "productListings" and d != "salesTransactions":
            response = "Error - Bad Request"
            return jsonify(response), 400
    
    #creating empty dictionaries and list
    product_listings = {}
    sales_transactions = {}
    authorization = []
    
    #adding data into dictionaries
    for listing in data.get("productListings", []):
        product_listings[listing["productID"]] = listing["authorizedSellerID"] #{'123': 'A1'}

    for transaction in data.get("salesTransactions", []):
        sales_transactions[transaction["productID"]] = transaction["sellerID"] #{'123': 'B2'}

    #authorization of the seller using id
    idSeler = "A1" # id of seller reached from database, since there's not database it's hardcoded
    for productIDSales, sellerID  in sales_transactions.items():
        for authorizedSellerID in product_listings.values():
            if idSeler == authorizedSellerID:
                authorization.append({"productID": productIDSales, "authorizedSellerID" : authorizedSellerID})
            else:
                authorization.append({"productID": productIDSales, "unauthorizedSellerID" : sellerID})


    #returning response with JSON data
    response = authorization
    return jsonify(response), 200
    