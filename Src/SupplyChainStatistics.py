"""
-------------------------------------------------------
This file contains and defines the SupplyChainStatistics class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 15th 2016
-------------------------------------------------------
"""

import matplotlib.pyplot as plt

class SupplyChainStatistics:
    
    def __init__(self):
        
        #Cost statistics
        self.retailerCostsOverTime = []
        self.wholesalerCostsOverTime = []
        self.distributorCostsOverTime = []
        self.factoryCostsOverTime = []
        
        #Order statistics
        
        return
    
    def RecordRetailerCost(self, retailerCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the retailer's record.
        -------------------------------------------------------
        Preconditions: retailerCostsThisWeek - the cost (dollars)
            incurred by the retailer during the given week.
        Postconditions: retailerCostsThisWeek is appended to 
            retailerCostsOverTime, a list which tracks the retailer's
            weekly costs.
        -------------------------------------------------------
        """
        self.retailerCostsOverTime.append(retailerCostsThisWeek)
        return
    
    def RecordWholesalerCost(self, wholesalerCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the wholesaler's record.
        -------------------------------------------------------
        Preconditions: wholesalerCostsThisWeek - the cost (dollars)
            incurred by the wholesaler during the given week.
        Postconditions: wholesalerCostsThisWeek is appended to 
            wholesalerCostsThisWeek, a list which tracks the wholesalers's
            weekly costs.
        -------------------------------------------------------
        """
        self.wholesalerCostsOverTime.append(wholesalerCostsThisWeek)
        return
    
    def RecordDistributorCost(self, distributorCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the distributor's record.
        -------------------------------------------------------
        Preconditions: distributorCostsThisWeek - the cost (dollars)
            incurred by the distributor during the given week.
        Postconditions: distributorCostsThisWeek is appended to 
            distributorCostsThisWeek, a list which tracks the distributor's
            weekly costs.
        -------------------------------------------------------
        """
        self.distributorCostsOverTime.append(distributorCostsThisWeek)
        return
    
    def RecordFactoryCost(self, factoryCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the factory's record.
        -------------------------------------------------------
        Preconditions: factoryCostsThisWeek - the cost (dollars)
            incurred by the factory during the given week.
        Postconditions: factoryCostsThisWeek is appended to 
            factoryCostsOverTime, a list which tracks the factory's
            weekly costs.
        -------------------------------------------------------
        """
        self.factoryCostsOverTime.append(factoryCostsThisWeek)
        return
    
    def PlotCosts(self):
        #Plot retailer cost
        plt.plot(self.retailerCostsOverTime, "r", label = "Retailer")
        plt.plot(self.wholesalerCostsOverTime, "g", label = "Wholesaler")
        plt.plot(self.distributorCostsOverTime, "b", label = "Distributor")
        plt.plot(self.factoryCostsOverTime, "m", label="Factory")
        legend = plt.legend(loc='upper left', shadow=True)
        plt.ylabel('Cost ($)')
        plt.xlabel("Weeks")
        plt.show()
        return
    
    