
import asyncio
import httpx
import time
from app.config import settings


REQUEST_COUNT = 1000
CONCURRENT_REQUESTS = 20

url = "http://localhost:8000/api/v1/predict"

data = {
    "sepallength": 5.1,
    "sepalwidth": 3.5,
    "petallength": 1.4,
    "petalwidth": 0.2
}

headers = {
    "X-API-Key": settings.API_KEY
}


async def send_request(client, semaphore):
    async with semaphore:
        try:
            response = await client.post(
                url,
                json=data,
                headers=headers
            )

            if response.status_code != 200:
                print(
                    "Status:",
                    response.status_code,
                    "Response:",
                    response.text
                )

            return response.status_code

        except Exception as e:
            print("Request error:", e)
            return None


async def main():

    start_time = time.perf_counter()

    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async with httpx.AsyncClient(timeout=30) as client:

        tasks = []

        for i in range(REQUEST_COUNT):
            tasks.append(
                send_request(client, semaphore)
            )

        results = await asyncio.gather(*tasks)

    total_duration=time.perf_counter()-start_time

    success = 0
    failed = 0

    for result in results:
        if result == 200:
            success += 1
        else:
            failed += 1

    print()
    print("Total requests:", REQUEST_COUNT)
    print("Successful requests:", success)
    print("Failed requests:", failed)
    print("Time taken:", round(total_duration,2), "seconds")
    print("Time taken:", f"{REQUEST_COUNT/total_duration:.2f}", "request")


if __name__ == "__main__":
    asyncio.run(main())

