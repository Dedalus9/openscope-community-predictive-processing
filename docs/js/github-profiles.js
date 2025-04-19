// GitHub handles mapping for team members
const GITHUB_PROFILES = {
  "Test": "test"
  // Add more team members here in the format "Full Name": "github-username"
};

// Function to get GitHub username by person's name
function getGitHubUsername(fullName) {
  return GITHUB_PROFILES[fullName] || null;
}

// Export the functions and data for use in other scripts
if (typeof module !== 'undefined') {
  module.exports = {
    GITHUB_PROFILES,
    getGitHubUsername
  };
}

// GitHub Profile Renderer - Site-wide version
document.addEventListener('DOMContentLoaded', function() {
    // Process GitHub handles in any element
    const processGitHubHandles = function() {
        // Find all text content that might contain GitHub handles
        // This includes paragraphs, list items, table cells, headings, etc.
        const elements = document.querySelectorAll('p, li, td, th, h1, h2, h3, h4, h5, h6, span, div');
        
        elements.forEach(function(element) {
            // Skip elements that are within profile cards (to avoid reprocessing)
            if (element.closest('.github-profile-card') || 
                element.closest('.profile-card')) {
                return;
            }
            
            // Use a regex to find GitHub handles (@username format)
            // that are not within email addresses
            const text = element.innerHTML;
            if (!text) return;
            
            // Pattern: space or start of string, followed by @, followed by letters/numbers/hyphens
            // Not preceded by text that would make it an email
            const pattern = /(^|\s)@([a-zA-Z0-9-]+)(?!\S*@)/g;
            
            // Replace all instances of GitHub handles with profile cards
            element.innerHTML = text.replace(pattern, function(match, prefix, username) {
                return `${prefix}<span class="github-handle" data-username="${username}">@${username}</span>`;
            });
        });
        
        // Now process all the handles we've wrapped
        const githubHandles = document.querySelectorAll('.github-handle');
        
        githubHandles.forEach(function(handle) {
            const username = handle.getAttribute('data-username');
            if (!username) return;
            
            // Create profile card container
            const cardContainer = document.createElement('div');
            cardContainer.className = 'github-profile-card';
            
            // Add loading indicator
            cardContainer.innerHTML = `<div class="loading">Loading ${username}'s profile...</div>`;
            
            // Insert card after the handle
            handle.parentNode.insertBefore(cardContainer, handle.nextSibling);
            
            // Fetch GitHub profile data - add error handling for rate limits
            fetch(`https://api.github.com/users/${username}`)
                .then(response => {
                    if (response.status === 403) {
                        // Likely a rate limit issue
                        throw new Error('GitHub API rate limit exceeded. Please try again later.');
                    }
                    if (!response.ok) {
                        throw new Error('GitHub profile not found');
                    }
                    return response.json();
                })
                .then(data => {
                    // Create profile card with GitHub data
                    cardContainer.innerHTML = `
                        <div class="profile-card">
                            <div class="profile-image">
                                <a href="${data.html_url}" target="_blank">
                                    <img src="${data.avatar_url}" alt="${username}'s avatar">
                                </a>
                            </div>
                            <div class="profile-info">
                                <h4><a href="${data.html_url}" target="_blank">${data.name || username}</a></h4>
                                ${data.bio ? `<p class="bio">${data.bio}</p>` : ''}
                            </div>
                        </div>
                    `;
                })
                .catch(error => {
                    // If fetching fails, just show a simple link
                    cardContainer.innerHTML = `<a href="https://github.com/${username}" target="_blank">@${username}</a>`;
                    console.error('Error fetching GitHub profile:', error);
                });
        });
    };
    
    // Add CSS for GitHub profiles
    const style = document.createElement('style');
    style.textContent = `
        .github-profile-card {
            margin: 10px 0;
        }
        .profile-card {
            display: flex;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 10px;
            background-color: #f6f8fa;
            max-width: 400px;
        }
        .profile-image img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .profile-info h4 {
            margin: 0 0 5px 0;
        }
        .profile-info .bio {
            margin: 0;
            font-size: 0.9em;
            color: #586069;
        }
        .loading {
            font-style: italic;
            color: #586069;
            font-size: 0.9em;
        }
    `;
    document.head.appendChild(style);
    
    // Run processor
    processGitHubHandles();
});