from fastapi import FastAPI

app = FastAPI(
    title="Online Cinema",
    description="digital platform that allows users to "
                "select, watch, and purchase access to movies and other video materials "
                "via the internet",
    version="1.0",
    contact={
        "email": "leonsiypopov@gmail.com",
        "url": "https://google.com",
        "name": "Leo",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)