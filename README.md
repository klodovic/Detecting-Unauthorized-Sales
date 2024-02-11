DETECTING UNAUTHORIZED SALES

OBJECTIVE:</br>
Develop a solution to identify unauthorized sales transactions from provided datasets of product listings and actual sales records.

TASK OVERVIEW</br>
The task is to develop a REST API endpoint that processes POST requests containing two lists: one containing product listing (including product ID and authorized seller ID) and the other actual sales transactions (including product ID and seller ID). Your task is to develop an algorithm that identifies any sales transactions made by unauthorized seller.

INSTRUCTIONS
1. Write a REST endpoint that receives a POST request with JSON data in a format similar to the one given in the following example:
{
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}

2. Implement an algorithm to compare the product listings against the sales transactions to identify unauthorized sales.
3. Return the response formatted in the following way:
{
  ": [
    {"productID": "123", "unauthorizedSellerID": ["B2"]}
  ]
}
4. Follow RESTful principles when designing your API endpoint. Ensure your API responds with appropriate HTTP status codes (e.g., 200 OK for successful requests, 400 Bad Request for invalid input).

EVALUATION CRITERIA
- Code Quality: Code readability, maintainability, simplicity, and adherence to best practices are essential.
- Correctness: Your algorithm must accurately determine the maximum number of interviews that can be attended, given the constraints.
- Efficiency: The solution should be optimized with regard to algorithmic time complexity.


<h1>Output</h1>

Unauthorized seller</br>
![task2-1](https://github.com/klodovic/Detecting-Unauthorized-Sales/assets/61901937/67fed730-0834-4994-bca4-289033ccab71)


Authorized seller</br>

![task2-2](https://github.com/klodovic/Detecting-Unauthorized-Sales/assets/61901937/d5175633-9273-4375-a0a5-f4bb03eed8b2)


Empty request</br>

![task2-4](https://github.com/klodovic/Detecting-Unauthorized-Sales/assets/61901937/c7ef91ed-b676-471f-8147-7f61559ed2e4)


Missing data</br>

![taks2-3](https://github.com/klodovic/Detecting-Unauthorized-Sales/assets/61901937/5f0e6d61-87f0-4c8d-a12f-8e94da6d5c79)

