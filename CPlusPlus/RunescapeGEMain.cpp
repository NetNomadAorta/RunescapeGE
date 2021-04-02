// RunescapeGEMain.cpp : This file contains the 'main' function.
// Purpose: to import Grand Exchange from OSRS Wiki and display data for 
//   selected items.
#define CURL_STATICLIB

#include <iostream>
#include <ctime>
#include <chrono>
#include <thread>

#include <json/json.h>

#include "curl_json.h"

Json::Value latest;

std::string unixToDate(int unixTime)
{
    // Function to convert unix-number to appropriate date format
    std::time_t time = unixTime;
    std::string date = ctime(&time);
    return date;
}

void show(std::string item)
{
    // Function to convert unix-number to appropriate date format
    std::cout << "\n";
    std::cout << "=== " << item << " ===\n";
    std::cout << latest[item] << std::endl;
}

int main()
{
    // URLs
    // ========================================================================
    // Json data of osrs mapping info: name, high alch value, etc.
    std::string urlMap("https://prices.runescape.wiki/api/v1/osrs/mapping");

    // Json data of latest osrs GE prices
    std::string urlLatest("https://prices.runescape.wiki/api/v1/osrs/latest");


    // Mapping - Sets mapping info for each item's id number
    // ========================================================================
    Json::Value jsonDataMap;
    jsonDataMap = scrape(urlMap); // Import json data from map url
    
    Json::Value map;
    
    for (auto i = jsonDataMap.begin(); i != jsonDataMap.end(); ++i)
    {
        // Display (*i)
        //std::cout << (*i) << std::endl;
        
        map[ (*i)["id"].asString() ]["name"] = (*i).get("name", "");
        map[ (*i)["id"].asString() ]["highalch"] = (*i).get("highalch", 0);
        map[ (*i)["id"].asString() ]["members"] = (*i).get("members", "");
        map[ (*i)["id"].asString() ]["limit"] = (*i).get("limit", "");
    }

    // Displays "map" mapping info
    //std::cout << map << std::endl;


    while (true)
    {
        // Latest - Sets and displays latest pricing and important info.
        // ====================================================================
        Json::Value jsonDataLatest;
        jsonDataLatest = scrape(urlLatest);
        jsonDataLatest = jsonDataLatest["data"]; //steps into 'data' key

        //Json::Value latest; // Not needed since forward declared up top

        // Sets useful information under "latest" such as high $, high-alch $
        for (auto i = jsonDataLatest.begin(); i != jsonDataLatest.end(); ++i)
        {
            // Display keys of jsonDataLatest
            //std::cout << i.key() << std::endl;

            latest[map[i.key().asString()]["name"].asString()]["1_high"]
                = (*i).get("high", 0);

            latest[map[i.key().asString()]["name"].asString()]["2_low"]
                = (*i).get("low", 0);
            /*
            latest[map[i.key().asString()]["name"].asString()]["3_highTime"]
                = unixToDate((*i).get("highTime", 0).asInt());

            latest[map[i.key().asString()]["name"].asString()]["4_lowTime"]
                = unixToDate((*i).get("lowTime", 0).asInt());
            */
            latest[map[i.key().asString()]["name"].asString()]["5_margin"]
                = (*i).get("high", 0).asInt() - (*i).get("low", 0).asInt();
            /*
            latest[map[i.key().asString()]["name"].asString()]["6_highAlch"]
                = map[i.key().asString()].get("highalch", 0);
            */
            latest[map[i.key().asString()]["name"].asString()]["7_alchProfit"]
                = map[i.key().asString()].get("highalch", 0).asInt()
                - (jsonDataLatest["561"]["high"].asInt()
                    + (*i).get("high", 0).asInt());
            /*
            latest[map[i.key().asString()]["name"].asString()]["8_id"]
                = i.key().asString();
            */
        }

        // Displays "latest" info including high price, margin, high-alch price
        //std::cout << latest << std::endl;


        // Displays latest GE info
        //std::cout << jsonDataLatest.toStyledString() << std::endl;
        //std::cout << jsonDataLatest.size() << std::endl;


        // Type item names to search for market info
        std::string item1 = "Rune javelin heads";
        std::string item2 = "Amethyst javelin heads";
        std::string item3 = "Abyssal bracelet(5)";
        std::string item4 = "Air battlestaff";
        std::string item5 = "Onyx bolts (e)";
        std::string item6 = "Onyx dragon bolts (e)";
        std::string item7 = "Emerald bracelet";
        std::string item8 = "Emerald";

        // Uses show function to display item info
        std::cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n";
        show(item1);
        show(item2);
        show(item3);
        show(item4);
        show(item5);
        show(item6);
        show(item7);
        show(item8);

        std::this_thread::sleep_for(std::chrono::seconds(5));
    }

    std::cout << "Press any key to exit.";
    int reeee;
    std::cin >> reeee;

    return 0;
}