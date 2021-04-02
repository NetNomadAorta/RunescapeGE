#pragma once

namespace
{
    std::size_t callback(
        const char* in,
        std::size_t size,
        std::size_t num,
        std::string* out);
}

Json::Value scrape(const std::string url);