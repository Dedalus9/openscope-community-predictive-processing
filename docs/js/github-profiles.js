// GitHub Profile Renderer - Site-wide version
document.addEventListener('DOMContentLoaded', function() {
    // Process GitHub handles in any element
    const processGitHubHandles = function() {
        // Create a container for all profile cards if multiple are present
        const mainContainer = document.createElement('div');
        mainContainer.className = 'github-profiles-container';
        let profilesAdded = 0;
        let currentRow = null;
        
        // Special handling for table cells with GitHub handles
        const tableCells = document.querySelectorAll('td');
        tableCells.forEach(function(cell) {
            const text = cell.textContent.trim();
            // Check if it's likely a GitHub handle cell
            if (text.startsWith('@')) {
                const username = text.substring(1);
                if (username && username.length > 0) {
                    // Replace the entire cell content with a span to avoid the @ appearing alone
                    cell.innerHTML = `<span class="github-handle-wrapper"><span class="github-handle" data-username="${username}"></span></span>`;
                }
            }
        });
        
        // Find all text content that might contain GitHub handles
        // This includes paragraphs, list items, headings, etc.
        const elements = document.querySelectorAll('p, li, h1, h2, h3, h4, h5, h6, span, div');
        
        elements.forEach(function(element) {
            // Skip elements that are within profile cards (to avoid reprocessing)
            if (element.closest('.github-profile-card') || 
                element.closest('.profile-card') ||
                element.closest('.github-handle-wrapper') ||
                element.closest('.github-profiles-container')) {
                return;
            }
            
            // Use a regex to find GitHub handles (@username format)
            // that are not within email addresses
            const text = element.innerHTML;
            if (!text) return;
            
            // Pattern: space or start of string, followed by @, followed by letters/numbers/hyphens
            // Not preceded by text that would make it an email
            const pattern = /(^|\s)@([a-zA-Z0-9-]+)(?!\S*@)/g;
            
            // Replace all instances of GitHub handles with profile cards - completely replace the match
            element.innerHTML = text.replace(pattern, function(match, prefix, username) {
                // Include the prefix (space) in the wrapper to avoid orphaned @ symbols
                return `<span class="github-handle-wrapper">${prefix}<span class="github-handle" data-username="${username}"></span></span>`;
            });
        });
        
        // Count total handle instances to decide on layout
        const githubHandles = document.querySelectorAll('.github-handle');
        const totalHandles = githubHandles.length;
        
        // If we have multiple handles, append the container to the document body
        // and prepare for a grid layout
        if (totalHandles > 1) {
            document.body.appendChild(mainContainer);
            currentRow = document.createElement('div');
            currentRow.className = 'github-profiles-row';
            mainContainer.appendChild(currentRow);
        }
        
        // Now process all the handles we've wrapped
        githubHandles.forEach(function(handle) {
            const username = handle.getAttribute('data-username');
            if (!username) return;
            
            // Create profile card container
            const cardContainer = document.createElement('div');
            cardContainer.className = 'github-profile-card';
            
            // Add loading indicator
            cardContainer.innerHTML = `<div class="loading">Loading GitHub profile...</div>`;
            
            // If multiple handles exist, add to the grid container
            if (totalHandles > 1) {
                if (profilesAdded > 0 && profilesAdded % 3 === 0) {
                    // Create a new row every 3 profiles
                    currentRow = document.createElement('div');
                    currentRow.className = 'github-profiles-row';
                    mainContainer.appendChild(currentRow);
                }
                currentRow.appendChild(cardContainer);
                profilesAdded++;
                
                // Hide the original handle wrapper
                const handleWrapper = handle.closest('.github-handle-wrapper');
                if (handleWrapper) {
                    handleWrapper.style.display = 'none';
                }
            } else {
                // Insert card after the handle wrapper for single profile case
                const handleWrapper = handle.closest('.github-handle-wrapper');
                if (handleWrapper) {
                    handleWrapper.parentNode.insertBefore(cardContainer, handleWrapper.nextSibling);
                } else {
                    handle.parentNode.insertBefore(cardContainer, handle.nextSibling);
                }
            }
            
            // Fetch GitHub profile data
            const headers = {
                'Accept': 'application/vnd.github.v3+json'
            };
            
            fetch(`https://api.github.com/users/${username}`, { headers })
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
                    // Create profile card with GitHub data - use real name if available, with handle underneath
                    const displayName = data.name || username;
                    
                    cardContainer.innerHTML = `
                        <div class="profile-card">
                            <div class="profile-image">
                                <a href="${data.html_url}" target="_blank">
                                    <img src="${data.avatar_url}" alt="${displayName}'s avatar">
                                </a>
                            </div>
                            <div class="profile-info">
                                <h4><a href="${data.html_url}" target="_blank">${displayName}</a></h4>
                                <p class="username">@${username}</p>
                                ${data.bio ? `<p class="bio">${data.bio}</p>` : ''}
                            </div>
                        </div>
                    `;
                    
                    // For single profile case, hide the original handle wrapper
                    if (totalHandles === 1) {
                        const handleWrapper = handle.closest('.github-handle-wrapper');
                        if (handleWrapper) {
                            handleWrapper.style.display = 'none';
                        }
                    }
                })
                .catch(error => {
                    // If fetching fails, just show a simple link
                    cardContainer.innerHTML = `<a href="https://github.com/${username}" target="_blank">@${username}</a>`;
                    console.error('Error fetching GitHub profile:', error);
                });
        });
        
        // If we added profiles to the grid, position it properly on the page
        if (profilesAdded > 0) {
            // Find a good location to insert the grid (near the first handle)
            const firstHandleWrapper = document.querySelector('.github-handle-wrapper');
            if (firstHandleWrapper && firstHandleWrapper.parentNode) {
                // Move from body to proper location in document
                document.body.removeChild(mainContainer);
                firstHandleWrapper.parentNode.insertBefore(mainContainer, firstHandleWrapper.nextSibling);
            }
        }
    };
    
    // Add CSS for GitHub profiles
    const style = document.createElement('style');
    style.textContent = `
        .github-profiles-container {
            margin: 20px 0;
            max-width: 100%;
        }
        .github-profiles-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 10px;
        }
        .github-profile-card {
            margin: 5px 0;
            flex: 1 1 calc(33.333% - 10px);
            min-width: 200px;
            max-width: calc(33.333% - 10px);
        }
        .profile-card {
            display: flex;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 10px;
            background-color: #f6f8fa;
            height: 100%;
        }
        .profile-image img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .profile-info h4 {
            margin: 0 0 5px 0;
            font-size: 0.95em;
        }
        .profile-info .username {
            margin: 0 0 5px 0;
            font-size: 0.8em;
            color: #586069;
        }
        .profile-info .bio {
            margin: 5px 0 0 0;
            font-size: 0.85em;
            color: #586069;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .loading {
            font-style: italic;
            color: #586069;
            font-size: 0.9em;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .github-profile-card {
                flex: 1 1 calc(50% - 10px);
                max-width: calc(50% - 10px);
            }
        }
        @media (max-width: 480px) {
            .github-profile-card {
                flex: 1 1 100%;
                max-width: 100%;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Run processor
    processGitHubHandles();
});