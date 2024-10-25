"""Pydantic schemas"""
from pydantic import BaseModel

class FantasyAcquistionFeatures(BaseModel):
    waiver_value_tier: int
    fantasy_regular_season_weeks_remaining: int
    league_budget_pct_remaining: int

class PredictionOutput(BaseModel):
    winning_bid_10th_percentile: float
    winning_bid_50th_percentile: float
    winning_bid_90th_percentile: float
