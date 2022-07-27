import ntfpy, asyncio

async def main():
    client = ntfpy.NTFYClient(ntfpy.NTFYServer("https://ntfy.sh"), "test", ntfpy.NTFYUser("user", "pass"))
    client.send("Hello World!")
    await client.subscribe()

asyncio.run(main())