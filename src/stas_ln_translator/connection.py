import httpx


async def create_translation_request(
    texts: list[str], client: httpx.AsyncClient, api_url: str, type: str
) -> list[str]:
    json_data = (
        {"batch": texts, "message": "translate batch"}
        if type == "Batch"
        else {
            "content": texts[0],
            "message": "translate sentences",
        }
    )

    response = await client.post(api_url, json=json_data)

    return list(response.json()) if type == "Batch" else [response.json()]
