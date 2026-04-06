"""
Meal Planning Workflow Orchestration

This module implements a workflow orchestration system for meal planning operations.
It manages the state transitions and data flow through the meal planning pipeline.
"""

from enum import Enum
from typing import Any, Dict, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class WorkflowState(Enum):
    """Enumeration of possible workflow states."""
    INITIALIZED = "initialized"
    PREFERENCES_SET = "preferences_set"
    SUGGESTIONS_GENERATED = "suggestions_generated"
    MEAL_PLAN_CREATED = "meal_plan_created"
    SHOPPING_LIST_GENERATED = "shopping_list_generated"
    COMPLETED = "completed"
    FAILED = "failed"


class MealPlanningWorkflow:
    """
    Orchestrates the meal planning workflow, managing state transitions
    and coordinating between different components of the system.
    """

    def __init__(self, user_id: str, workflow_id: Optional[str] = None):
        """Initialize the workflow."""
        self.user_id = user_id
        self.workflow_id = workflow_id or f"{user_id}_{datetime.now().timestamp()}"
        self.state = WorkflowState.INITIALIZED
        self.metadata: Dict[str, Any] = {}
        self.error_log: list = []
        logger.info(f"Workflow {self.workflow_id} initialized for user {user_id}")

    def set_preferences(self, preferences: Dict[str, Any]) -> bool:
        """Set user preferences for meal planning.""" 
        try:
            self.metadata["preferences"] = preferences
            self.state = WorkflowState.PREFERENCES_SET
            logger.info(f"Preferences set for workflow {self.workflow_id}")
            return True
        except Exception as e:
            logger.error(f"Error setting preferences: {str(e)}")
            self.error_log.append(str(e))
            self.state = WorkflowState.FAILED
            return False

    def generate_suggestions(self, suggestions: list) -> bool:
        """Generate recipe suggestions based on preferences.""" 
        try:
            self.metadata["suggestions"] = suggestions
            self.state = WorkflowState.SUGGESTIONS_GENERATED
            logger.info(f"Suggestions generated for workflow {self.workflow_id}")
            return True
        except Exception as e:
            logger.error(f"Error generating suggestions: {str(e)}")
            self.error_log.append(str(e))
            self.state = WorkflowState.FAILED
            return False

    def create_meal_plan(self, meal_plan: Dict[str, Any]) -> bool:
        """Create a meal plan from selected recipes.""" 
        try:
            self.metadata["meal_plan"] = meal_plan
            self.state = WorkflowState.MEAL_PLAN_CREATED
            logger.info(f"Meal plan created for workflow {self.workflow_id}")
            return True
        except Exception as e:
            logger.error(f"Error creating meal plan: {str(e)}")
            self.error_log.append(str(e))
            self.state = WorkflowState.FAILED
            return False

    def generate_shopping_list(self, shopping_list: Dict[str, Any]) -> bool:
        """Generate a shopping list from the meal plan.""" 
        try:
            self.metadata["shopping_list"] = shopping_list
            self.state = WorkflowState.SHOPPING_LIST_GENERATED
            logger.info(f"Shopping list generated for workflow {self.workflow_id}")
            return True
        except Exception as e:
            logger.error(f"Error generating shopping list: {str(e)}")
            self.error_log.append(str(e))
            self.state = WorkflowState.FAILED
            return False

    def complete(self) -> bool:
        """Mark the workflow as completed.""" 
        try:
            self.metadata["completed_at"] = datetime.now().isoformat()
            self.state = WorkflowState.COMPLETED
            logger.info(f"Workflow {self.workflow_id} completed successfully")
            return True
        except Exception as e:
            logger.error(f"Error completing workflow: {str(e)}")
            self.error_log.append(str(e))
            self.state = WorkflowState.FAILED
            return False

    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the workflow.""" 
        return {
            "workflow_id": self.workflow_id,
            "user_id": self.user_id,
            "state": self.state.value,
            "metadata": self.metadata,
            "error_log": self.error_log,
        }